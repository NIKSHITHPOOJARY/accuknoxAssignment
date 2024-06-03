import psutil

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Check CPU usage
def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    print(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: CPU usage is above {CPU_THRESHOLD}%")

# Check memory usage
def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")
    if memory_usage > MEMORY_THRESHOLD:
        print(f"ALERT: Memory usage is above {MEMORY_THRESHOLD}%")

# Check disk usage
def check_disk_usage():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    print(f"Disk Usage: {disk_usage}%")
    if disk_usage > DISK_THRESHOLD:
        print(f"ALERT: Disk usage is above {DISK_THRESHOLD}%")

# Check running processes
def check_running_processes():
    processes = len(psutil.pids())
    print(f"Running Processes: {processes}")

# Main function to check system health
def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_running_processes()

if __name__ == "__main__":
    main()
