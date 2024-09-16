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
    return {
        "Buffer Size": buffer_size / 1024,  # Convert to KB
        "Time Taken": end_time - start_time,
        "Initial CPU Usage": initial_cpu,
        "Final CPU Usage": final_cpu,
        "Initial Memory Usage": initial_mem,
        "Final Memory Usage": final_mem
    }

# No Compression, no buffering
def without_compression(input_file, buffer_size=8192):
    """Copy the file with buffered I/O, without compression."""
    start_time = time.time()

    # Monitor CPU and memory usage
    process = psutil.Process(os.getpid())
    initial_cpu = process.cpu_percent(interval=None)
    initial_mem = process.memory_info().rss / (1024 * 1024)

    with open(input_file, 'rb') as f_in:
        with open("uncompressed_copy.txt", 'wb') as f_out:
            buffered_writer = io.BufferedWriter(f_out, buffer_size=buffer_size)
            while True:
                data = f_in.read(buffer_size)
                if not data:
                    break
                buffered_writer.write(data)

    # Final benchmarking metrics
    end_time = time.time()
    final_cpu = process.cpu_percent(interval=None)
    final_mem = process.memory_info().rss / (1024 * 1024)

    return {
        "Buffer Size": buffer_size / 1024,
        "Time Taken": end_time - start_time,
        "Initial CPU Usage": initial_cpu,
        "Final CPU Usage": final_cpu,
        "Initial Memory Usage": initial_mem,
        "Final Memory Usage": final_mem
    }

# Run multiple tests with different configurations
def run_benchmarks(input_file):
    """Run benchmarks with different buffer sizes and compression/no compression."""
    buffer_sizes = [4096, 8192, 16384, 32768]  # Buffer sizes: 4KB, 8KB, 16KB, 32KB
    results = []

    print("\n--- Compression with Buffered I/O ---")
    for buffer_size in buffer_sizes:
        result = compress_with_buffering(input_file, 'compressed_data.lz4', buffer_size=buffer_size)
        print(f"Buffer Size: {result['Buffer Size']} KB, Time: {result['Time Taken']:.2f}s, "
              f"Initial CPU: {result['Initial CPU Usage']:.1f}%, Final CPU: {result['Final CPU Usage']:.1f}%, "
              f"Memory: {result['Initial Memory Usage']:.2f}MB -> {result['Final Memory Usage']:.2f}MB")
        results.append(result)

    print("\n--- No Compression with Buffered I/O ---")
    for buffer_size in buffer_sizes:
        result = without_compression(input_file, buffer_size=buffer_size)
        print(f"Buffer Size: {result['Buffer Size']} KB, Time: {result['Time Taken']:.2f}s, "
              f"Initial CPU: {result['Initial CPU Usage']:.1f}%, Final CPU: {result['Final CPU Usage']:.1f}%, "
              f"Memory: {result['Initial Memory Usage']:.2f}MB -> {result['Final Memory Usage']:.2f}MB")
        results.append(result)
    
    return results

# Simulate large data generation (HPC simulation, 100MB)
input_file = 'large_data.txt'

# Step 1: Generate large data (e.g., 100 MB file)
generate_large_data(input_file, size_in_mb=100)

# Step 2: Run benchmarks
benchmark_results = run_benchmarks(input_file)

# Clean-up (optional)
os.remove(input_file)
os.remove('compressed_data.lz4')
os.remove('uncompressed_copy.txt')
