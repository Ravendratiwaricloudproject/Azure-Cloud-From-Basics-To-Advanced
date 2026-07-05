# Day-12 - Introduction to Azure Load Balancing Services


# What are Azure Load Balancing Services?

The term load balancing refers to the distribution of processing across multiple computing resources. You load balance to optimize resource usage, maximize throughput, minimize response time, and avoid overloading any single resource. Load balancing can also improve availability by sharing a workload across redundant computing resources.

Azure provides various load balancing services that you can use to distribute your workloads across multiple computing resources.


 
 
 
 
 
 1. Azure Load Balancer:

Load Balancer is a Layer 4 (Transport Layer) load balancer service that distributes incoming traffic across multiple backend servers.

Load Balancer handles inbound and outbound traffic across all User Datagram Protocol (UDP) and Transmission Control Protocol (TCP) protocols. 

It's designed for high performance and ultra-low latency. It's built to handle millions of requests per second while ensuring that your solution is highly available.

Types of Azure Load Balancer:

* Standard Load Balancer
   
Recommended for production workloads.
Higher availability and scalability.
More secure by default.
Supports Availability Zones and larger backend pools.
It can be Public or Internal


* Gateway Load Balancer
  
Gateway Load Balancer is a SKU (Stock Keeping Unit) in the Azure Load Balancer portfolio.
It is designed for high performance and high availability scenarios involving third-party Network Virtual Appliances (NVAs).

With Gateway Load Balancer, you can easily deploy, scale, and manage NVAs.
It allows you to transparently insert appliances into network traffic flow, such as:

Firewalls
Advanced packet inspection tools
Intrusion Detection and Prevention Systems (IDS/IPS)
Traffic mirroring solutions
DDoS protection appliances
Custom network/security appliances



# What is a Network Virtual Appliance (NVA)?

An NVA is a virtual machine that acts as a network device. Instead of forwarding traffic directly to your application, it can inspect, filter, or protect the traffic.
Note: Azure-native NVAs: Azure Firewall & Azure Application Gateway



Note: Most NVAs come from security/network companies such as:

Palo Alto Networks
Fortinet
Check Point Software Technologies
Cisco




2. Application Gateway

Azure Application Gateway is a Layer 7 (Application Layer) load balancer designed specifically for web applications.

Features:

Distributes HTTP and HTTPS traffic.

Routes requests based on:
URL path
Hostname
HTTP headers

Supports SSL/TLS termination.

Supports Web Application Firewall (WAF).

Enables session affinity (sticky sessions).

Mainly used for web applications.

It works at Layer 7 (Application layer) of the OSI model.




3. Application Gateway for Containers:

It is an application layer (layer 7) load balancing and dynamic traffic management product for workloads running in a Kubernetes cluster.

It is used to distributes web traffic for Azure Kubernetes service (AKS) workloads.


4. Azure Front Door(Content delivery):


Azure Front Door is an application delivery network that provides global load balancing and site acceleration for web applications.

 It provides Layer-7 capabilities for your application such as Secure Sockets Layer (SSL) offload, path-based routing, fast failover, and caching to improve performance and high availability.

5. Azure API Management:

API Management is a managed service that you can use to publish, secure, transform, maintain, and monitor HTTP(S) APIs. It provides a gateway for your APIs and can be configured to load balance traffic across nodes in a designated load balanced back-end pool. You can choose from three different load balancing methods: round-robin, weighted, and priority-based.

Important
API Management isn't a traditional, general-purpose load balancer. It's designed specifically for HTTP APIs, and its load balancing capabilities are optional within its broader API management functionality. API Management is included in this article for completeness because it provides load balancing capabilities for specific API hosting topologies. However, its primary purpose is API gateway functionality rather than load balancing.




6. Azure Traffic Manager(DNS load balancing):

Traffic Manager is a Domain Name System (DNS)-based traffic load balancer that enables you to distribute traffic optimally to services across global Azure regions, while providing high availability and responsiveness.

 Because Traffic Manager is a DNS-based load balancing service, it load balances only at the domain level. For that reason, it can't fail over as quickly as Azure Front Door. DNS caching and systems that ignore DNS time-to-live (TTL) values often cause this delay.






