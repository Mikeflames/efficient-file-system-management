import time
import numpy as np
from io_optimization import optimize_io_operations

def benchmark_io():
    start_time = time.time()
    optimize_io_operations(100)  # Benchmark I/O for 100 MB data
    end_time = time.time()
    print(f"Benchmark time: {end_time - start_time} seconds")

if __name__ == "__main__":
    benchmark_io()
