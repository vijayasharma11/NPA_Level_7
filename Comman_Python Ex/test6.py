import matplotlib.pyplot as plt
from matplotlib.dates import date2num
from datetime import datetime

# Task Data for Gantt Chart
tasks = [
    {"Task": "Requirement Gathering", "Start": "2023-06-01", "End": "2023-06-05"},
    {"Task": "Design Navigation Menu", "Start": "2023-06-06", "End": "2023-06-12"},
    {"Task": "Plan Product Categories", "Start": "2023-06-13", "End": "2023-06-19"},
    {"Task": "Development of Display", "Start": "2023-06-20", "End": "2023-07-15"},
    {"Task": "Implement Search Features", "Start": "2023-07-16", "End": "2023-07-25"},
    {"Task": "Testing and Debugging", "Start": "2023-07-26", "End": "2023-08-05"},
    {"Task": "Deployment and Launch", "Start": "2023-08-06", "End": "2023-08-31"},
]

# Convert dates and calculate positions for Gantt Chart
y_pos = range(len(tasks))
start_dates = [date2num(datetime.strptime(task["Start"], "%Y-%m-%d")) for task in tasks]
end_dates = [date2num(datetime.strptime(task["End"], "%Y-%m-%d")) for task in tasks]
durations = [end - start for start, end in zip(start_dates, end_dates)]

# Create Gantt Chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(y_pos, durations, left=start_dates, color='skyblue', edgecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels([task["Task"] for task in tasks])
ax.set_xlabel("Timeline")
ax.set_title("Gantt Chart for Web Gallery Project")

# Format the x-axis to display dates
ax.xaxis_date()
plt.tight_layout()
plt.show()
