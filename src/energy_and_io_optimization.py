import numpy as np
import time

def optimized_io_operation(data, operation='read'):
    start_time = time.time()
    
    if operation == 'read':
        # Simulate efficient data read operation
        processed_data = np.array(data)
    elif operation == 'write':
        # Simulate efficient data write operation
        processed_data = np.array(data)
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f"{operation.capitalize()} operation completed in {elapsed_time:.6f} seconds.")
    return processed_data

def energy_optimized_algorithm(data):
    # Example of energy-efficient algorithm
    result = np.sqrt(data)  # Example of an operation that could be optimized for energy
    return result

if __name__ == "__main__":
    # Example usage
    data = np.random.rand(1000, 1000)  # Large dataset for testing
    
    # Optimize I/O operations
    optimized_io_operation(data, operation='read')
    optimized_io_operation(data, operation='write')
    
    # Apply energy-optimized algorithm
    result = energy_optimized_algorithm(data)
    print("Energy-optimized algorithm completed.")
