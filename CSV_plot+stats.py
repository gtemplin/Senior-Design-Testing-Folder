import pandas as pd
import matplotlib.pyplot as plt
import os 
import math

# Replace 'your_file_path.csv' with the actual path to your CSV file
CSV_file_name = input("Enter the CSV file name: ")
file_path = f'/home/gtemplin/Senior Design Testing Folder (FINAL)/performance_logs/{CSV_file_name}'


def printStats(col_stats, col_name):
    print(f"Stats for {col_name}")
    print(f"Minimum: {col_stats[0]}")
    print(f"Maximum: {col_stats[1]}")
    print(f"Average: {col_stats[2]}")
    print(f"Standard Deviation: {col_stats[3]}\n\n")


def print_stats(stats_list):
    # Print the header
    print(f"\n\n\n{'Metric':<20} {'Min':<10} {'Max':<10} {'Average':<10} {'Std Dev':<10}")
    print("-" * 60)  # Print a separator line
    
    # Iterate through the list of stats and print each one
    for stats in stats_list:
        title, min_val, max_val, average, stdev = stats
        print(f"{title:<20} {min_val:<10} {max_val:<10} {average:<10} {stdev:<10}")
    print("\n\n\n")


def getStats(csv_file, column_name):
    df = pd.read_csv(csv_file)
    column = df[column_name]
    title = column_name
    min = column.min()
    max = column.max()
    average = column.mean()
    stdev = column.std()
    stats = [title, min, max, round(average,2), round(stdev,2)]
    return stats


def round_to_nearest_10(n):
    """Rounds a number to the nearest 10."""
    return 10 * round(n / 10)

def find_extremes_and_round(stats_list):
    # Extract all minimum and maximum values from the stats list
    all_mins = [stats[1] for stats in stats_list]
    all_maxs = [stats[2] for stats in stats_list]
    
    # Find the smallest minimum and the largest maximum
    smallest_min = min(all_mins)
    largest_max = max(all_maxs)
    
    # Round these values to the nearest 10
    rounded_min = round_to_nearest_10(smallest_min)
    rounded_max = round_to_nearest_10(largest_max)
    
    return rounded_min, rounded_max

################# Calculate Statistics ################
temp_stats = getStats(file_path, "Temperature")
mem_stats = getStats(file_path, "Memory Free %")
cpu_stats = getStats(file_path, "CPU Utilization %")

allStats = [temp_stats, mem_stats, cpu_stats]

min, max = find_extremes_and_round(allStats)

print_stats(allStats)




# Define your file path for saving
save_path = f'/home/gtemplin/Senior Design Testing Folder (FINAL)/performance_plots/{CSV_file_name}.png'
# Check if the file already exists
if os.path.exists(save_path):
    print(f"The file '{save_path}' already exists. File not saved.")
    exit(1)


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
ax1.set_ylim(min, max)
ax1.plot(df['Seconds Since Start'], df['Temperature'], color=color, label='Temperature (°C)')
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Percentage', color=color)
ax2.set_ylim(min, max)
ax2.plot(df['Seconds Since Start'], df['Memory Free %'], color='tab:green', label='Memory Free %')
ax2.plot(df['Seconds Since Start'], df['CPU Utilization %'], color=color, label='CPU Utilization %')
ax2.tick_params(axis='y', labelcolor=color)

# Adjust layout and title position
fig.tight_layout()
plt.subplots_adjust(top=0.85)  # Adjust top spacing to fit title
fig.legend(loc="upper right", bbox_to_anchor=(1, 1))  #, bbox_to_anchor=(0.1,0.9))
plt.title('CPU Metrics', y=1.05, fontsize=25)  # Adjust title position

plt.savefig(save_path)

