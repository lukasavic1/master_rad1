import matplotlib.pyplot as plt
import json


def read_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

file_name = 'perf/perf_stats_test2_RAFT.json'
write_data = read_json(file_name)['write_data']

# Extract the duration of each operation
durations = [operation["duration"] for operation in write_data]

# file_name = 'res.txt'
# with open(file_name, 'r') as f:
#     durations = f.readlines()
# durations = [float(duration) for duration in durations]
# print(durations)

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(range(len(durations)), durations, 'o', markersize=5, color='blue')

# Label the axes
plt.xlabel('Broj zahteva')
plt.ylabel('Trajanje [sec]')
plt.title('Latencije svih zahteva sa RAFT implementacijom')

# Display the plot
plt.show()
