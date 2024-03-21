import pandas as pd
import matplotlib.pyplot as plt


# Replace 'your_file_path.csv' with the actual path to your CSV file
CSV_file_name = '2024-03-21_10-49-16.csv'
file_path = f'/home/admin/Senior-Design-Testing-Folder/performance_logs/{CSV_file_name}'

# Reading the CSV file
df = pd.read_csv(file_path, parse_dates=['Datetime'])

# Calculating seconds since the start
df['Seconds Since Start'] = (df['Datetime'] - df['Datetime'].iloc[0]).dt.total_seconds()

# The plotting code remains the same
fig, ax1 = plt.subplots()

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

fig.tight_layout()
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9))
plt.title('CPU Metrics')
plt.show()
