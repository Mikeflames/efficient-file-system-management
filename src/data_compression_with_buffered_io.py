import os
import lz4.frame  # LZ4 compression library
import io         # For Buffered I/O
import time       # To measure performance
import psutil     # To monitor memory and CPU usage
import random     # To simulate large data input
import string

# Function to generate large random data (simulating HPC logs/data)
def generate_large_data(file_path, size_in_mb=100):
    """Generates a large random text file for compression benchmarking."""
    with open(file_path, 'w') as f:
        for _ in range(size_in_mb * 1024):  # 1 MB = 1024 KB
            # Writing 1 KB chunks of random data
            f.write(''.join(random.choices(string.ascii_letters + string.digits, k=1024)))

# Buffered I/O and Compression
def compress_with_buffering(input_file, output_file, buffer_size=8192):
    """Compress data using LZ4 with Buffered I/O."""
    start_time = time.time()  # Start time for benchmarking
    
    # Monitor CPU and memory usage
    process = psutil.Process(os.getpid())
    initial_cpu = process.cpu_percent(interval=None)
    initial_mem = process.memory_info().rss / (1024 * 1024)  # Convert to MB

    with open(input_file, 'rb') as f_in:
        with lz4.frame.open(output_file, mode='wb') as compressed_file:
            buffered_writer = io.BufferedWriter(compressed_file, buffer_size=buffer_size)
            while True:
                data = f_in.read(buffer_size)
                if not data:
                    break
                buffered_writer.write(data)

    # Final benchmarking metrics
    end_time = time.time()
    final_cpu = process.cpu_percent(interval=None)
    final_mem = process.memory_info().rss / (1024 * 1024)  # Convert to MB

    # Benchmarking output
    print(f"--- Data Compression with Buffered I/O ---")
    print(f"Buffer Size: {buffer_size / 1024} KB")
    print(f"Time Taken: {end_time - start_time:.2f} seconds")
    print(f"Initial CPU Usage: {initial_cpu}% | Final CPU Usage: {final_cpu}%")
    print(f"Initial Memory Usage: {initial_mem:.2f} MB | Final Memory Usage: {final_mem:.2f} MB")

# Simulate large data generation (HPC simulation, 100MB)
input_file = 'large_data.txt'
output_file = 'compressed_data.lz4'

# Step 1: Generate large data (e.g., 100 MB file)
generate_large_data(input_file, size_in_mb=100)

# Step 2: Benchmark and compress data with buffered I/O and LZ4 compression
compress_with_buffering(input_file, output_file)

# Clean-up (optional)
os.remove(input_file)
os.remove(output_file)
