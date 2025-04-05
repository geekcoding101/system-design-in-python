import os
import random
from datetime import datetime

# Path for the log file
LOG_FILE = "syslog.log"


# Function to generate a syslog-style log file
def generate_syslog(num_lines=1000):
    """
    Generates a simulated syslog file, where each line represents a log entry.
    Format Example:
    "Mar 5 12:34:56 myserver process[1234]: Log message"
    """
    hostnames = ["server1", "server2", "server3"]
    processes = ["sshd", "nginx", "docker", "kernel", "systemd"]
    log_levels = ["INFO", "WARNING", "ERROR", "DEBUG"]

    with open(LOG_FILE, "w") as f:
        for i in range(1, num_lines + 1):
            timestamp = datetime.now().strftime("%b %d %H:%M:%S")
            hostname = random.choice(hostnames)
            process = random.choice(processes)
            pid = random.randint(1000, 9999)
            level = random.choice(log_levels)
            message = f"Log ID {i}: {level} - Example log message {i}"
            log_entry = f"{timestamp} {hostname} {process}[{pid}]: {message}\n"
            f.write(log_entry)


# Sparse Indexing
def build_sparse_index(log_file, step=100):
    """
    Creates a sparse index by storing log_id -> file offset every 'step' lines.
    This reduces the number of indexed entries while allowing fast lookups.
    """
    sparse_index = {}
    with open(log_file, "r") as f:
        line_num = 1  # Track line number manually
        while True:
            current_offset = f.tell()  # Store the offset before reading the line
            line = f.readline()
            if not line:
                break  # Stop at EOF

            # Ensure the line contains "Log ID"
            if "Log ID" in line:
                try:
                    log_id = int(line.split("Log ID")[1].split(":")[0].strip())
                    if line_num % step == 0:  # Store an index entry every 'step' lines
                        sparse_index[log_id] = current_offset
                except (IndexError, ValueError):
                    print(f"Skipping malformed log entry: {line.strip()}")

            line_num += 1  # Increment line counter

    return sparse_index


# Memory Table Indexing
def build_memory_table(log_file, max_size=500):
    """
    Maintains an in-memory hash index (log_id -> file offset).
    When the index grows beyond 'max_size', it writes a new segment file and clears memory.
    """
    memory_table = {}  # In-memory index
    persistent_segments = []  # List of segment files

    with open(log_file, "r") as f:
        while True:
            current_offset = f.tell()  # Store the offset before reading the line
            line = f.readline()
            if not line:
                break  # Stop at EOF

            # Ensure the line contains "Log ID" before processing
            if "Log ID" in line:
                try:
                    log_id = int(line.split("Log ID")[1].split(":")[0].strip())
                    memory_table[log_id] = (
                        current_offset  # Store the offset of this log_id
                    )
                except (IndexError, ValueError):
                    print(f"Skipping malformed log entry: {line.strip()}")

            # When memory table exceeds max_size, flush it to a segment file
            if len(memory_table) >= max_size:
                segment_file = f"log_segment_{len(persistent_segments) + 1}.index"
                with open(segment_file, "w") as seg_f:
                    for key, value in memory_table.items():
                        seg_f.write(f"{key},{value}\n")
                persistent_segments.append(segment_file)
                memory_table.clear()  # Clear in-memory index

    return memory_table, persistent_segments


# Function to search for a log entry using indexes
def search_log(log_file, log_id, sparse_index, memory_table):
    """
    Searches for a log entry using sparse index or in-memory hash index.
    Falls back to scanning from the nearest sparse index if the log is not found in memory.
    """
    with open(log_file, "r") as f:
        # Check memory index first
        if log_id in memory_table:
            f.seek(memory_table[log_id])
            return f.readline()

        # Find the nearest index entry in sparse index
        closest_id = max([i for i in sparse_index.keys() if i <= log_id], default=None)
        if closest_id is None:
            return None  # Log ID is out of range

        # Seek to the closest known offset and scan forward
        f.seek(sparse_index[closest_id])
        for line in f:
            if f"Log ID {log_id}:" in line:
                return line
    return None  # Log ID not found


# Run example
generate_syslog(1000)  # Generate a log file with 1000 entries
sparse_index = build_sparse_index(LOG_FILE, step=100)  # Build sparse index
memory_table, segment_files = build_memory_table(
    LOG_FILE, max_size=500
)  # Build memory index

log_id_to_search = 257  # Example log ID to search
found_log = search_log(LOG_FILE, log_id_to_search, sparse_index, memory_table)
print(f"Found log entry: {found_log}")
