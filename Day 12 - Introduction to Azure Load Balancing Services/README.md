# Day-12 - Introduction to Azure Load Balancing Services

# What are Azure Load Balancing Services?

Azure Load Balancing is a service that automatically distributes incoming network traffic across multiple Virtual Machines (VMs) or other backend resources to improve application availability, scalability, and reliability.

# Types of Load Balancing Services in Azure:

In Azure, there are two types of load Balancing services:

1. Load Balancer

2. Application Gateway


# Azure Load Balancer

Azure Load Balancer is a Layer 4 (Transport Layer) load balancer service that distributes incoming traffic across multiple backend servers.

Features:

Distributes incoming network traffic across multiple VMs.

Performs health probes to monitor backend VM health.

Stops sending traffic to unhealthy VMs.

It works with VMs and Virtual Machine Scale Sets.

It can be public or private.

It operates at Layer 4 (Transport layer) of the OSI model.

Types of Azure Load Balancer:

Basic Load Balancer

Standard Load Balancer

Difference between Basic and Standard Load Balancer:

Basic Load Balancer:

Suitable for small or testing environments.
Limited features.
Lower scalability.

Standard Load Balancer:

Recommended for production workloads.
Higher availability and scalability.
More secure by default.
Supports Availability Zones and larger backend pools.

In simple words:

Basic Load Balancer → Small or test environments

Standard Load Balancer → Production environments


# Azure Application Gateway

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


# Difference between Azure Load Balancer and Application Gateway:


| Azure Load Balancer              | Azure Application Gateway               |
| -------------------------------- | --------------------------------------- |
| Works at Layer 4                 | Works at Layer 7                        |
| Handles TCP/UDP traffic          | Handles HTTP/HTTPS traffic              |
| Basic traffic distribution       | Intelligent web traffic routing         |
| No URL-based routing             | Supports URL and host-based routing     |
| No WAF support                   | Supports Web Application Firewall (WAF) |
| Used for any network application | Used for web applications               |


In simple words:

Azure Load Balancer is used for basic traffic distribution.

Application Gateway is used for smart routing of web traffic with more advanced features

