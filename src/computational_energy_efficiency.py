import time
import psutil  # For CPU usage
import numpy as np  # For matrix operations
import os

def energy_consumption(cpu_usage, time_taken, power_factor=0.5):
    """
    Estimate energy consumption based on CPU usage and time taken.
    Assumes power consumption is proportional to CPU usage and duration.
    
    :param cpu_usage: The percentage of CPU utilization
    :param time_taken: Time in seconds the operation took
    :param power_factor: A scaling factor for energy consumption (in watts per CPU percentage)
    :return: Estimated energy consumption in joules (Watts * seconds)
    """
    # Power consumption (in watts) = CPU usage (%) * power_factor (watts per % usage)
    power_consumption = cpu_usage * power_factor
    # Energy (in joules) = power (in watts) * time (in seconds)
    energy = power_consumption * time_taken
    return energy

def matrix_multiplication(size):
    """
    Simulates a heavy computational task (matrix multiplication) commonly used in HPC.
    
    :param size: Size of the square matrices to multiply
    :return: Time taken and energy consumed during the operation
    """
    # Generate random matrices
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)

    # Measure CPU usage before and after
    cpu_usage_before = psutil.cpu_percent(interval=0.1)

    # Perform matrix multiplication
    start_time = time.time()
    result = np.dot(A, B)
    end_time = time.time()

    # Measure CPU usage again after completion
    cpu_usage_after = psutil.cpu_percent(interval=0.1)

    time_taken = end_time - start_time
    avg_cpu_usage = (cpu_usage_before + cpu_usage_after) / 2  # Average CPU usage during the task

    # Estimate energy consumption
    energy_used = energy_consumption(avg_cpu_usage, time_taken)
    
    return time_taken, energy_used

if __name__ == "__main__":
    matrix_size = 1000  
    time_taken, energy_used = matrix_multiplication(matrix_size)
    
    print(f"Matrix multiplication time: {time_taken:.4f} seconds")
    print(f"Estimated energy consumption: {energy_used:.4f} joules")
