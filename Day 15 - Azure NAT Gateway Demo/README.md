# Day 15 - Introduction to Azure NAT Gateway

# What is Azure NAT Gateway?

- Note: NAT stands for Network Address Translation.

An Azure NAT Gateway is a networking service provided by Microsoft Azure that allows outbound internet connectivity for resources in a virtual network (VNet) without exposing those resources directly to the internet.

We can use Azure NAT Gateway to let all instances in a private subnet connect outbound to the internet while remaining fully private.

Using a NAT Gateway, resources in private subnets can initiate communication with the public internet, but the public internet cannot initiate communication with those resources.

# When to Use Azure NAT Gateway:

1. Outbound Internet Access from Private Subnets:

- Your resources (e.g., VMs, containers) don’t have public IPs but need to access the internet (e.g., for software updates, API calls, etc.).

2. Static Outbound IP Address Requirement:

- You want all outbound traffic to use a consistent public IP address or range, especially useful when:
  
  Third-party services require IP whitelisting.

  You need consistent logs or audits of IP usage.

3. Large-Scale or High-Throughput Workloads:

- You expect thousands of connections or high bandwidth usage and need automatic scaling without manually managing IPs or SNAT ports.

4. Improved Security Posture:

- You want resources to initiate connections only, with no inbound exposure, unlike load balancers or public IPs.


5. Centralized Outbound Management:

- You want a central point to control and manage all outbound internet traffic from multiple resources or subnets.

# Azure NAT Gateway provides outbound connectivity for many Azure resources, including:

• Azure virtual machines or virtual machine scale-sets in a private subnet.

• Azure Kubernetes Services (AKS) clusters.

• Azure Container group.

• Azure Function Apps.

• Azure Firewall subnet.

• Azure App Services instances (web applications, REST APIs, and mobile backends) through virtual network integration.

• Azure Databricks or with virtual network injection.

• And more.

# Note: In AWS, the equivalent of Azure NAT Gateway is " NAT Gateway "

