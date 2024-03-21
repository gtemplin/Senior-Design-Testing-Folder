import pandas as pd
import matplotlib.pyplot as plt
import os 

# Replace 'your_file_path.csv' with the actual path to your CSV file
CSV_file_name = input("Enter the CSV file name: ")
file_path = f'/home/gtemplin/Senior Design Testing Folder (FINAL)/performance_logs/{CSV_file_name}'

# Define your file path for saving
save_path = f'/home/gtemplin/Senior Design Testing Folder (FINAL)/performance_plots/{CSV_file_name}.png'
# Check if the file already exists
if os.path.exists(save_path):
    print(f"The file '{save_path}' already exists. File not saved.")
    exit(1)



def getStats(csv_file, column_name):
    df = pd.read_csv(csv_file)
    column = df[column_name]
    min = column.min()
    max = column.max()
    average = column.mean()
    stdev = column.std()
    stats = [min, max, round(average,2), round(stdev,2)]
    return stats

def printStats(col_stats, col_name):
    print(f"Stats for {col_name}")
    print(f"Minimum: {col_stats[0]}")
    print(f"Maximum: {col_stats[1]}")
    print(f"Average: {col_stats[2]}")
    print(f"Standard Deviation: {col_stats[3]}\n\n")


################# Calculate Statistics ################
temp_stats = getStats(file_path, "Temperature")
printStats(temp_stats, "Temperature")
mem_stats = getStats(file_path, "Memory Free %")
printStats(mem_stats, "Memory Free %")
cpu_stats = getStats(file_path, "CPU Utilization %")
printStats(cpu_stats, "CPU Utilization %")




################# Generate the PNG file ################

# Reading the CSV file
df = pd.read_csv(file_path, parse_dates=['Datetime'])

# Calculating seconds since the start
df['Seconds Since Start'] = (df['Datetime'] - df['Datetime'].iloc[0]).dt.total_seconds()

# Specify figure size
fig, ax1 = plt.subplots(figsize=(10, 6.1))  # Adjust figure size as needed

color = 'tab:red'
ax1.set_xlabel('Seconds Since Start')
ax1.set_ylabel('Temperature (°C)', color=color)
ax1.plot(df['Seconds Since Start'], df['Temperature'], color=color, label='Temperature (°C)')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Percentage', color=color)
ax2.plot(df['Seconds Since Start'], df['Memory Free %'], color='tab:green', label='Memory Free %')
ax2.plot(df['Seconds Since Start'], df['CPU Utilization %'], color=color, label='CPU Utilization %')
ax2.tick_params(axis='y', labelcolor=color)

# Adjust layout and title position
fig.tight_layout()
plt.subplots_adjust(top=0.85)  # Adjust top spacing to fit title
fig.legend(loc="upper right", bbox_to_anchor=(1, 1))  #, bbox_to_anchor=(0.1,0.9))
plt.title('CPU Metrics', y=1.05, fontsize=25)  # Adjust title position

plt.savefig(save_path)

