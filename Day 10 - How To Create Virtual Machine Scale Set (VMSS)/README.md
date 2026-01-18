# What is Virtual Machine Scale Sets (VMSS)?

Azure Virtual Machine Scale Sets (VMSS) let you create and manage a group of virtual machines (VM).
The number of VM can automatically increase or decrease in response to demand or a defined schedule.
It's especially useful for applications that need to scale out (more instances) or scale in (reduce instances) automatically based on demand.

Note: The equivalent of Azure Virtual Machine Scale Sets (VMSS) in AWS is Auto Scaling Group (ASG).

# Why Scale set (VMSS)?

Use a scale set when you want your application to handle changes in traffic smoothly, stay resilient, and be easy to manage at scale.

Its Allows your application to automatically scale as resource demand changes.

Note: Azure VM Scale Sets can automatically monitor metrics (like CPU usage, memory, queue length, etc.) and perform scale in/out actions based on your defined auto scale rules.

# What is mean by Scale Out and Scale In?

Scale Out and Scale In refer to changing the number of VM /instances based on demand.

# Scale Out (Horizontal Scaling Out):

Scale out is about, adding more VM/ instances to the scale set.

•	Why it's used:
When your application is getting more traffic or workload than the current VMs can handle.

•	Example:
Suppose, you have 3 VMs running, but CPU usage is consistently above 80%. The scale set adds 2 more VMs to handle the load based on defined scaling policy in the scale set→ now you have 5 VMs.

# Scale In (Horizontal Scaling In):

Scale in is about, removing VM/ instances from the scale set.

•	Why it's used:

To save costs when demand goes down and when minimum VMs quantity are needed.

•	Example:
Your app is now seeing low traffic late at night, and CPU usage drops below 20%. The scale set removes 2 VMs → now you're running 3 VM instead of 5.



##########################################################################################################################################
Action        Description	                   Goal
Scale Out	    Add more VMs	            Handle more load
Scale In	    Remove VMs	             Save cost on low usage
##########################################################################################################################################


# What is Vertical Scaling (Scale Up / Scale Down)?

Vertical scaling means increasing or decreasing the size (power) of a single virtual machine instead of changing the number of VMs.

Instead of adding more VM, you make an existing VM bigger or smaller by changing its resources.

Scale Up (Vertical Scaling Up):

Scale up means increasing the resources of a VM, such as:

More CPU cores

More RAM

Faster or larger disk

Moving to a larger VM size (SKU)

Why it’s used:

When your application needs more power per VM, but adding more VMs is not ideal or possible.

Example:

You have 1 VM with:

2 vCPUs

4 GB RAM

Your application becomes slow due to high memory usage.

You scale up the VM to:

4 vCPUs

16 GB RAM

Now The VM becomes more powerful, but you still have only 1 VM.


Scale Down (Vertical Scaling Down):

Scale down means reducing the resources of a VM when high performance is no longer needed.

Why it’s used:

To reduce costs when workload decreases.

Example:

After peak hours, your app no longer needs high resources.

You scale the VM down from:

8 vCPUs → 2 vCPUs

32 GB RAM → 8 GB RAM

Now Same VM, just smaller and cheaper.

# Benefits of the Virtual Machine Scale Sets:

•	Easy to create and manage multiple VMs.

•	Provides high availability and application resiliency by distributing VMs across availability zones or fault domains.

•	Allows your application to automatically scale as resource demand changes.

•	Works at large-scale.

•	A group of separate VMs sharing the same image.

•	Managed as a group.

•	Can be scaled out or in manually or according to predefined conditions.

•	Great for handling unpredictable load.

•	Once set up, the machines should NOT be modified.

•	We can Change files, install apps etc.

•	New machines created by the scale set will be based on the original image.

•	VMSS can automatically increase or decrease the number of VM instances based on CPU usage, memory, disk I/O, or other custom metrics.

•	Scale sets can be integrated with Azure Load Balancer or Azure Application Gateway to distribute traffic across all instances.


# Virtual Machine Scale Sets Pricing:

•	Scale Set is free

•	You pay for the VMs deployed in it

