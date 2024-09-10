import time
import numpy as np

def optimize_io_operations(size_mb):
    start_time = time.time()
    data = np.random.rand(size_mb * 1024 * 1024 // 8)  # Generate random data
    end_time = time.time()
    print(f"Time taken to generate data: {end_time - start_time} seconds")

if __name__ == "__main__":
    optimize_io_operations(10)  # Optimize I/O for 10 MB data
