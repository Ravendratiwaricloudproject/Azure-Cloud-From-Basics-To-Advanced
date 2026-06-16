# Day 10: Azure Virtual Machine Scale Sets (VMSS)

## What is Azure Virtual Machine Scale Sets (VMSS)?

Azure Virtual Machine Scale Sets (VMSS) allow you to create and manage a group of Virtual Machines (VMs).

The number of VMs can automatically increase or decrease based on:

* Application demand
  
* Resource usage (CPU, Memory, etc.)
  
* A defined schedule

Virtual Machine Scale Sets is especially useful for applications that need to automatically scale out when traffic increases and scale in when traffic decreases.

**Note:** The equivalent service in AWS is **Auto Scaling Group (ASG)**.

## Why Do We Need VMSS?

We need VMSS because it helps applications to:

* Handle traffic spikes automatically
  
* Improve availability and reliability
  
* Reduce manual management
  
* Optimize costs by scaling resources based on demand

- Azure VM Scale Sets can monitor metrics such as:

* CPU usage
  
* Memory usage
  
* Disk activity
  
* Queue length
  
* Custom metrics

Based on these metrics, VMSS can automatically add or remove VM instances.

# What is Horizontal Scaling?

Horizontal Scaling is the process of adding or removing VM instances based on workload demand. Adding instances is called Scale Out, and removing instances is called Scale In.

Horizontal Scaling means increasing or decreasing the number of servers (VMs/instances) to handle changes in workload.

Instead of making a single VM more powerful, you add or remove VM instances.

- Why we Use Horizontal Scaling?

We Use Horizontal Scaling to:

 * Handles increased traffic efficiently

 * Improves application availability

 * Provides better fault tolerance

 * Helps to optimize costs by removing unused resources

# Types of Horizontal Scaling:

1. Scale Out

Adding more VM instances when demand increases.

### Why is it used?

When application traffic increases and the existing VMs cannot handle the load.

### Example

Suppose you have 3 VMs running.

* CPU usage stays above 80%.
* VMSS automatically adds 2 more VMs.

Result:

3 VMs → 5 VMs

This helps distribute the workload and improve performance.


2. Scale In

Removing VM instances when demand decreases.

### Why is it used?

To reduce costs when application demand decreases.

### Example

During late-night hours:

* Traffic decreases.
* CPU usage drops below 20%.
* VMSS removes 2 VMs.

Result:

5 VMs → 3 VMs

This saves money by running only the required number of VMs.


# What is Vertical Scaling (Scale Up / Scale Down)?

Vertical Scaling means increasing or decreasing the resources of a single VM instead of changing the number of VMs.

Instead of adding more VMs, you make the existing VM more powerful or less powerful.

# Type of Vertical Scaling?

1. Scale Up (Vertical Scaling)

Scale Up means increasing the resources of a VM, such as:

* More CPU cores
* More RAM
* Faster storage
* Larger VM size (SKU)

### Why is it used?

When an application needs more computing power on a single VM and adding more VMs is not practical.

### Example

Current VM:

* 2 vCPUs
* 4 GB RAM

Application performance becomes slow because of high memory usage.

After scaling up:

* 4 vCPUs
* 16 GB RAM

Result:

The VM becomes more powerful, but you still have only one VM.


2. Scale Down (Vertical Scaling)

Scale Down means reducing the resources of a VM when high performance is no longer needed.

### Why is it used?

To save costs during periods of low workload.

### Example

Before:

* 8 vCPUs
* 32 GB RAM

After Scale Down:

* 2 vCPUs
* 8 GB RAM

Result:

The same VM continues to run, but at a lower cost.

---

# Horizontal Scaling vs Vertical Scaling?

| Horizontal Scaling                   | Vertical Scaling                                  |
| ------------------------------------ | ------------------------------------------------- |
| Adds or removes VMs                  | Changes VM size                                   |
| Scale Out / Scale In                 | Scale Up / Scale Down                             |
| Better for high traffic applications | Better for applications needing more power per VM |
| Improves availability                | Limited by maximum VM size                        |

---

# Benefits of Azure VM Scale Sets (VMSS)

* Easy to deploy and manage multiple VMs
* Provides high availability and application resiliency
* Automatically scales based on workload demand
* Supports large-scale applications
* All VMs can be created from the same image
* Managed as a single group
* Ideal for handling unpredictable traffic
* New VM instances are automatically created from the original image
* Supports automatic scaling based on:

  * CPU usage
  * Memory usage
  * Disk I/O
  * Custom metrics
* Can integrate with:

  * Azure Load Balancer
  * Azure Application Gateway

---

# VMSS Pricing

The Virtual Machine Scale Set service itself is free.

You only pay for:

* Virtual Machines
* Storage
* Networking resources
* Other Azure services used by the VMs

