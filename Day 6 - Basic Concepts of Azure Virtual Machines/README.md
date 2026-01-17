# Basic Concepts of Azure Virtual Machines

# What is Virtual Machines (VM)?

•	It is computing service of Azure.

•	In Azure, it’s called VM (Virtual Machines)

•	In AWS, it’s called EC2 Instance

•	An Azure Virtual Machine (VM) is a cloud-based computing resource provided by Microsoft Azure, which is part of their cloud platform. 

It allows you to run an operating system (OS) and software just like you would on a physical computer, but instead of using your local hardware, the VM runs on the cloud infrastructure.

# What is Computing Service?

the Compute Service refers to the collection of resources and services designed to allow you to run and manage virtualized computing workloads.
These services provide the infrastructure, platform, and tools to run applications, host websites, process data, and much more—all in the cloud.


# Here are some Important Computing services under Azure Compute:

1. Virtual Machines

2. App Services

3. Azure Functions

4. AKS

# Types (Category) of Virtual Machines on Azure:

Azure provides a variety of virtual machine (VM) offerings to cater to different workload requirements. Each VM type is designed with specific hardware configurations to meet diverse performance and scalability needs.

1. General Purpose:
   
Example: Standard_D2s_v3
Description:  General-purpose VMs are well-balanced machines suitable for a variety of workloads.
They offer a good balance of CPU-to-memory ratio and are suitable for development, testing, and small to medium-sized databases.
Use Case: Hosting websites, lightweight applications, or development and testing environments.

3. Compute Optimized:
   
Example: Standard_F2s_v2
Description: Compute optimized VMs are designed for compute-intensive workloads that require high CPU power.
They provide a high CPU-to-memory ratio, making them suitable for data analytics and computational tasks.
Use Case: Batch processing, gaming applications, and other CPU-intensive workloads.

5. Memory Optimized:
   
Example: Standard_E16s_v3
Description: Memory optimized VMs are tailored for memory-intensive applications. They provide a high memory-to-CPU ratio, making them  suitable for databases, in-memory caching, and analytics.
Use Case: Running large databases, in-memory caching, and analytics applications.

7. Storage Optimized:
   
Example: Standard_L8s_v2
Description: Storage optimized VMs are designed for workloads that require high storage throughput and I/O performance.
They provide high local disk throughput, making them suitable for big data and large databases.
Use Case: Big data applications, data warehousing, and large-scale databases.

9. GPU (Graphics Processing Unit):
    
Example: Standard_NC6s_v3
Description: GPU (Graphics Processing Unit) VMs are equipped with powerful graphics processors,
suitable for graphics-intensive applications and parallel processing tasks.
Use Case: Machine learning, graphics rendering, and simulations that require GPU acceleration.

11. High-Performance Compute VMs:
    
Example: Standard_H16r
Description: High-Performance Compute VMs are designed for demanding, parallel processing and high-performance computing (HPC) applications.
Use Case: Simulations, modelling, and scenarios that require massive parallel processing.

# Reducing the Cost of VM Using Azure Saving Plans:

 What is mean by Saving Plans?
In Azure, Saving Plans are a flexible pricing model, that offers low prices on Azure VM

1. Reserve Instances:
   
•	It provides significant discount (up to 62%)

•	Usually offered for 1 or 3 years

•	Great for production machine which run continuously

•	Can be divided to monthly payments

•	Cannot be stopped / refunded

3. Spot Instances:
   
•	We can use spot Instance on spare VM capacity that is available for less than on-demand price.

•	Machines that run on unused capacity in Azure

•	Can be evicted any moment when needed by Azure

•	Offers up to 90% discount, price fluctuates according to demand

•	Great for non-critical, non-continuous tasks

	i.e. Batch processes, long running calculations

# More Cost Saving Techniques:

1. Disk Optimization:
   
•	Choose the right disk for the machine.

•	The default disk is Premium SSD, which is the most expensive option.

•	Machines that don’t require a lot of input/output (IO) can use Standard SSD.

•	For example, app servers or in-memory caches.

•	Keep in mind: The disk type impacts the service level agreement (SLA).

3. Auto Shutdown:
   
•	Automatically shuts down the machine when not needed

•	Relevant mainly for test / dev machines

•	Storage and IP (if static) costs still incurred
•	Can save  50% of VM cost

5.	Select the right size for your machine

6. Select Linux over Windows when possible:
   
i.e. if you have a choice, you should choose Linux instead of Windows for your system or application.

This could be because Linux is often more cost-effective, secure, or efficient for certain tasks, especially in server or cloud environments.

8. Check price in nearby regions



