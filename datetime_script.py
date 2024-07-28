from datetime import datetime

# List of time strings
times = ["2023-07-24 14:30:00", "2023-07-24 11:15:00", "2023-07-24 17:45:00"]

# Convert time strings to datetime objects
datetime_objects = [datetime.strptime(time, "%Y-%m-%d %H:%M:%S") for time in times]

print("Data time objects:", datetime_objects)

# Find the minimum datetime
min_time = min(datetime_objects)
print(min_time)
print(type(min_time))

# Format the minimum datetime
formatted_min_time = min_time.strftime("%Y-%m-%d %H:%M:%S")

print(formatted_min_time)
print(type(formatted_min_time))