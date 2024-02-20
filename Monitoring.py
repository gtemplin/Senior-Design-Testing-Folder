import sys, os
import subprocess
#sudo apt-get python-psutil??? - easier, but might not be able to use with docker installed on pi

def get_cpu_temperature():

    output = subprocess.check_output(["vcgencmd", "measure_temp"])
    temp = float(output.split("=")[1][:-3])
    return temp

print(get_cpu_temperature())

#needs tested/ checked

#import psutil

#def get_ram_usage():


  #ram = psutil.virtual_memory()
  #ram_percent_used = ram.percent
  #return ram_percent_used

#if __name__ == "__main__":
 # ram_usage = get_ram_usage()
 # print("RAM used is {}%.".format(ram_usage))
