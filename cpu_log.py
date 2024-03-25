# Here's a Python script to get the CPU temperature and memory utilization of a Raspberry Pi.
import datetime
import os
import atexit 
import time
import csv
import sys 

container_to_stop = "test"  # stop the container in emergency case  

starting_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

main_directory = "/home/admin/Senior-Design-Testing-Folder"
if os.path.exists(main_directory):
    print("Path exists")

# Disk storage logs. Don't want to use these for frequent writes, only intermittently 
SD_card_path = f'/home/admin/Senior-Design-Testing-Folder/performance_logs/{starting_datetime}.csv'

if os.path.exists(SD_card_path):
    os.remove(SD_card_path)
    print("Removed SD Card Log")
else:
    print("Was no SD Card Log")


# Frequently written to 
RAM_storage_path = f'/dev/shm/temp_performance_logs_{starting_datetime}.csv'
if os.path.exists(RAM_storage_path):
    os.remove(RAM_storage_path)
    print("Removed Temp RAM Log")
else: 
    print("Was no RAM Log ")


# Write to the CSV file stored in RAM 
def ram_log(message):
    with open(RAM_storage_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(message)  
ram_log(["Datetime","Temperature","Memory Free %","CPU Utilization %"]) # Generate CSV Title 

# Function to save the RAM stored file to the SD card (disk storage)
def save_to_disk():
    # Ensure the directory exists
    os.makedirs(os.path.dirname(SD_card_path), exist_ok=True)
    # Check if the RAM disk file exists and is not empty
    if os.path.exists(RAM_storage_path) and os.path.getsize(RAM_storage_path) > 0:
        # Get the data from the ram file and store it in a list 
        with open(RAM_storage_path, 'r') as ram_file:
            ram_reader = csv.reader(ram_file)
            data = list(ram_reader)
        # Write the list to the SD card 
        with open(SD_card_path, 'a') as disk_file:
            print(f"Writing to SD card: {SD_card_path}")
            disk_writer = csv.writer(disk_file)
            for row in data:
                print(row)
                disk_writer.writerow(row)
        os.remove(RAM_storage_path)  # Clean up the RAM disk file
save_to_disk() 


# Returns the CPU temp in deg celcius 
def get_cpu_temperature():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temp_str = file.read()
            # The temperature is reported in thousandths of degrees Celsius. For example, 45007 means 45.007°C.
            # Let's convert it to a float in degrees Celsius.
            temp_c = float(temp_str) / 1000
            return temp_c
    except FileNotFoundError:
        return "Temperature sensor not found. Are you running this on a Raspberry Pi?"

# Stops the python program if CPU temperature exceeds 70 deg celcius 
def temperatureSafetyCheck():
    cpu_temp = get_cpu_temperature()
    #print(f"CPU Temperature: {cpu_temp} °C")
    if cpu_temp < 70:
        #print("Within safe range (under 70°C)")
        return "safe"
    elif cpu_temp >= 70:
        print("CPU exceeds recommended temperature. Stopping python program")
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"Stopped program at {current_datetime} due to overheating"
        ram_log(message)
	# stop the test container 
        import subprocess
        command = ['docker', 'stop', container_to_stop]
        result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Container {container_to_stop} stopped successfully.")
        print(result.stdout)
    else:
        print(f"Failed to stop container {container_to_stop}.")
        print(result.stderr) 
    exit(1) 


# This returns the percentage of the total RAM that is free to do work
def get_ram_usage():
    with open("/proc/meminfo", "r") as meminfo:
        meminfo_lines = meminfo.readlines()
    mem_total = 0
    mem_available = 0
    # Parse the necessary values
    for line in meminfo_lines:
        if "MemTotal" in line:
            mem_total = int(line.split()[1])
        elif "MemAvailable" in line:
            mem_available = int(line.split()[1])
    
    # Calculate the percentage of available memory
    if mem_total > 0:  # Prevent division by zero
        available_memory_percentage = (mem_available * 100.0) / mem_total
        return available_memory_percentage
    else:
        return "Memory total is zero, can't calculate percentage."

# Returns the cpu utilization percentage for all cores 
def read_cpu_usage():
    """Reads CPU usage statistics from /proc/stat."""
    with open("/proc/stat", "r") as f:
        line = f.readline()
        # Extract the CPU time spent in various modes from the first line
        cpu_times = [float(value) for value in line.split()[1:]]
    return cpu_times

# Calcualte the CPU utilization in a 1 second period 
def calculate_cpu_usage(delay=1):
    start_times = read_cpu_usage()
    time.sleep(delay)
    end_times = read_cpu_usage()

    # Calculate time spent in each of the modes over the delay period
    delta_times = [end - start for start, end in zip(start_times, end_times)]
    total_delta_time = sum(delta_times)

     # Calculate the percentage of time spent idle / total time 
    idle_time = delta_times[3]  # The 4th value in the list corresponds to idle time
    idle_percentage = (idle_time / total_delta_time) * 100
    
    # Subtract idle percentage from 100 to get CPU utilization
    cpu_usage_percentage = 100 - idle_percentage
    return round(cpu_usage_percentage, 2)

# gets all of the metrics and packs them in a dictionary  
def createMessage():
    CPU_temp = round(get_cpu_temperature(), 2)
    temperatureSafetyCheck()
    RAM_free_pct = round(get_ram_usage(), 2)
    CPU_util_pct = round(calculate_cpu_usage(),2)
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = [current_datetime, CPU_temp, RAM_free_pct, CPU_util_pct]
    return message


# 2880 minutes in 48 hours 
# 576 5

if __name__ == "__main__":
    print("Starting prolonged test")
    args = []
    for i, arg in enumerate(sys.argv[1:], 1):
        print(arg)
        args.append(arg)
    numLogs = int(args[0])
    print(numLogs)

    delayBetweenReads = 30 # seconds between each writing 
    totalLogsDesired = numLogs # how many logs 
    diskWriteFrequency = 100 # how many logs in between saving to the disk 
    runHrs = round((totalLogsDesired*delayBetweenReads)/60/60, 2)
    print(f"Will run for about {runHrs} hours")
    

    atexit.register(save_to_disk) # call the save to disk function when finished 

    logCount = 0
    while True:
        logCount += 1
        if logCount % diskWriteFrequency != 0:
            ram_log(createMessage())
        else:
            save_to_disk() # every 250 logs, save to the disk and flush out the RAM storage 
        if logCount >= totalLogsDesired:
            ram_log(["Exited", "with", "code", "0"])
            exit(0) # indicates the test ran successfully after some number of readings 
        print(f"Log {logCount}")
        time.sleep(delayBetweenReads) # wait for a bit to not overload the RAM/disk 


# If just using the functions 
else:
    print("Imported cpu_log")
