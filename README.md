# Efficient File System Management and Energy Optimization

## Overview

This project implements a distributed file system management system with a focus on optimizing storage, I/O performance, and energy consumption across HPC, Cloud, and Edge computing environments.

## Features

- **File Storage Management**: Distributed file system with data replication and fault tolerance.
- **I/O Optimization**: Techniques for reducing latency and increasing throughput.
- **Energy Optimization**: Algorithms for minimizing energy consumption.
- **Performance Benchmarking**: Tools to benchmark and compare storage and I/O strategies.
- **User Interface**: Web-based or command-line interface for system management.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/efficient-file-system-management.git
   ```

2. Navigate to the project directory:

    ```
    cd efficient-file-system-management
    ```

3. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage
   Data-Compression with Buffered I/O
   
      python src/data_compression_with_buffered_io.py
      python src/data_compression_with_var_buffers.py
      
   Start the file system management system:
     
     python src/file_system.py

   Run the Computation_Energy_Simulation:
   
      python src/computational_energy_efficiency.py
        
   Run the I/O optimization and energy optimization modules:
   
        python src/io_optimization.py  
        python src/energy_optimization.py

   Run the Module for both Energy and I/O optimization:
   
        python src/energy_and_io_optimization.py  

   Use the benchmarking tools to measure performance:
   
        python src/benchmark.py
    
   Access the web interface (if applicable) by navigating to http://localhost:5000.

## Results for Data Compression with Buffered I/O :
1. Buffer Size: 8.0 KB  (  A smaller buffer size can lead to more frequent disk I/O, while a larger buffer size may reduce disk access frequency but consume more memory.)
2. Time Taken: 0.24 seconds  ( total time taken to compress the 100MB of data, LZ4 is a fast compression algorithm, known for both speed and energy efficiency, making this a good choice for your scenario)
3. Initial CPU Usage: 0.0% | Final CPU Usage: 26.6%  ( compression and buffering consumed moderate CPU resources during execution. This rise shows that the CPU was engaged in both reading the data, compressing it, and managing the buffered I/O.
4. Initial Memory Usage: 15.86 MB | Final Memory Usage: 15.99 MB (   The small increase in memory usage (from 15.86 MB to 15.99 MB) shows that buffered I/O and compression are memory-efficient. The buffer (8KB) and compression metadata have a minimal impact on memory consumption. )

## Results for Data Compression with Variable Buffers :
1. Compression with Buffered I/O  ( Buffer Size 4 KB, 8 KB, 16 KB, 32 KB) :-  The 8 KB buffer size seems to offer the most efficient compression, using significantly less CPU while maintaining a low processing time. Increasing the buffer size beyond 8 KB doesn't lead to significant performance gains in time, but it increases CPU usage.
2. No Compression with Buffered I/O  (  Buffer Size 4 KB, 8 KB, 16 KB, 32 KB) :-  For non-compressed data, larger buffer sizes (32 KB) offer better performance in terms of time and CPU usage. The benefit of increasing buffer size is more pronounced here than with compression.

By using these benchmarks, I can fine-tune the buffer size to align with my system's processing power, memory constraints, and the nature of the I/O workload.



## Future Scope
The current project provides a robust foundation for exploring advanced topics in storage, I/O, file systems, and energy optimization in HPC, Cloud, and Edge computing environments. Future enhancements and extensions include:

1. Scalability Enhancements:

   - Distributed Storage Systems: Implement and test distributed file systems to handle larger datasets and improve fault tolerance.
   - Cloud Integration: Extend the project to integrate with cloud storage solutions, optimizing data access and processing across cloud environments.

2. Energy Efficiency:

   - Energy-Aware Algorithms: Develop and incorporate energy-efficient algorithms for storage and I/O operations to reduce the overall power consumption of HPC systems.
   - Real-Time Monitoring: Implement real-time energy monitoring and adaptive management strategies to optimize energy usage based on workload and system performance.

3. Advanced File Systems:

   - File System Benchmarking: Add support for benchmarking various file systems (e.g., Lustre, GPFS) to compare performance and efficiency.
   - Custom File Systems: Explore the creation and testing of custom file systems tailored for specific applications or environments.

4. Edge Computing Optimization:

   - Data Caching: Develop and evaluate caching mechanisms for edge computing scenarios to reduce latency and improve data access times.
   - Resource Management: Implement dynamic resource management strategies for edge devices to balance workload and optimize performance.

5. Machine Learning Integration:

   - Predictive Analysis: Use machine learning models to predict storage needs and optimize I/O operations based on historical data and usage patterns.
   - Automated Tuning: Develop algorithms for automated tuning of storage and I/O parameters to enhance system efficiency.

## Learnings So Far
Throughout this project, significant learnings have been achieved in the following areas:

1. Performance Optimization:

   - Benchmarking Techniques: Gained expertise in benchmarking and analyzing performance metrics for storage and I/O operations.
   - Optimization Strategies: Developed and applied strategies for optimizing file system performance and energy efficiency.

2. Advanced File Systems:

   - Implementation and Testing: Acquired hands-on experience in implementing and testing various file systems, understanding their strengths and limitations.
   - Customization: Learned to customize file systems to meet specific project requirements and performance goals.

3. Energy Optimization:

   - Energy-Aware Computing: Explored techniques for reducing energy consumption in HPC and cloud environments, including algorithmic and system-level optimizations.
   - Monitoring Tools: Implemented tools for monitoring energy usage and performance, gaining insights into energy-efficient computing practices.

4. Edge Computing:

   - Resource Management: Enhanced understanding of resource management strategies for edge computing, including data caching and dynamic workload balancing.
   - Latency Reduction: Learned methods to reduce latency and improve data access times in distributed edge environments.
   
5. Technical Skills:

   - Programming: Advanced skills in Python and MPI for parallel computing.
   - System Integration: Improved ability to integrate and manage complex systems involving storage, file systems, and energy optimization.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Documentation
For detailed documentation, see the docs/index.md file.

## Contact
For questions or further discussions, please contact:
   - Mishal Singhai [Email](mailto:mishalsinghai21032001@gmail.com)
     
## References
- "Distributed Systems: Concepts and Design" by George Coulouris, Jean Dollimore, Tim Kindberg, and Gordon Blair
- "High Performance Parallel I/O" by Prabhat, Suren Byna, et al.
- Web-Resources

