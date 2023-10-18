processes = [("P1", 0, 10), ("P2", 2, 5), ("P3", 4, 7)]
quantum = 4

total_time = 0
remaining_processes = list(processes)

while remaining_processes:
    current_process = remaining_processes.pop(0)
    process_name, arrival_time, burst_time = current_process
    if arrival_time > total_time:
        total_time = arrival_time
    time_slice = min(quantum, burst_time)
    total_time += time_slice
    remaining_time = burst_time - time_slice
    if remaining_time > 0:
        remaining_processes.append((process_name, total_time, remaining_time))

print(total_time)