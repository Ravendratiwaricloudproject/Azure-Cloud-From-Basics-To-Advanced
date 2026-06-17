## Day 5: Azure Networking

---

## What is Virtual Networks (VNets)?

A Virtual Network, or VNet, is your private network inside Azure. Think of it as your company's own data center network, but running in Microsoft's cloud.

- It is a Virtual network or Data center inside Azure for one client.  
- It is logically Isolated from other virtual networks.  
- It is a network in which you can deploy cloud resources.  
- Many cloud resources are deployed within VNets. Ex. VMs, App Services, DBs, etc.  
- Think of it as your organization’s private network.  
- In AWS it’s called VPC – Virtual Private Cloud. Other organizations’ VNets.  
- Resources in the same VNet can communicate with each other by default.  
- But not with resources in other VNets.  
- To establish connection between two VNet, we can use VNet Peering.

---

## Characteristics of VNets:

- Scoped to a single Region  
- Cannot span multiple Regions  
- A VNet is created inside a subscription, but VNets can be peered across subscriptions and even across tenants.  
- Can be connected two VNets via Peering  
- Protected using NSGs and Azure Firewall  
- Can connect to on-premises networks  

---

## Addresses of VNets:

- Each VNet has its own IP address range.  
- By default, a VNet can contain up to 65,536 IP addresses (/16 address space), but this can be customized.  
- All resources and network devices within a VNet must use IP addresses from the VNet's defined address space.  
- IP address ranges are expressed using CIDR (Classless Inter-Domain Routing) notation.  
- Two VNets cannot be peered if they have overlapping or identical IP address spaces, including their subnets, as this  would cause address conflicts and routing issues.

---

## What is Addressing?

Addressing is the method used in computer networking to identify and locate devices so that data can be sent to the correct destination.

---

## Type of Addressing:

### Physical Addressing
- IP Address  
- MAC Address (48 bits)  

### Logical Addressing
- IPV6 (128 bits)  
- IPV4 (32 bits)  
- Private IP  
- Public IP  

---

## What is a MAC Address?

A MAC (Media Access Control) Address is a unique identifier assigned to a device's Network Interface Card (NIC) by the manufacturer. It acts like the device's physical identity on a network.  
MAC addresses are used to identify and communicate with devices within the same Local Area Network (LAN) and operate at Layer 2 (Data Link Layer) of the OSI Model  

### Key Points:
- MAC Address is a physical address.  
- Assigned by the device manufacturer.  

---

## What is IP (Internet Protocol)?

IP is a Logical address comprises of ‘4’ octet and each octet is differentiated by dot (.)  
IP address is used to provide communication between device over the internet.  

---

## Type of IPv4 Address:

### (1) Private IP:
- It is work at LAN  
- It is used to communicate within the same network  
- It is available free of cost  
- Private IP is secure  
- It is required NAT to communicate with device on internet  

#### Private IP range:
- 10.0.0.0 – 10.255.255.255  
- 172.16.0.0 – 172.31.255.255  
- 192.168.0.0 – 192.168.255.255  

---

### Public IP:
- It is work at WAN  
- It is used to communicate outside the network  
- It is used to get internet service  
- It is not available free of cost  
- Public IP is not secure  
- It is not required NAT to communicate with device on internet  

## IP Address Class:

- IP addressing is divided into different classes based on the range of IP addresses.  
- These classes are used to organize networks of different sizes.  
- Each class has a default subnet mask and supports a different number of hosts.  

---

### Class A:
- Range: 1.0.0.0 to 126.255.255.255  
- Default Subnet Mask: 255.0.0.0 (/8)  
- Supports very large networks  
- Used by large organizations  

---

### Class B:
- Range: 128.0.0.0 to 191.255.255.255  
- Default Subnet Mask: 255.255.0.0 (/16)  
- Supports medium-sized networks  
- Used by universities and large companies  

---

### Class C:
- Range: 192.0.0.0 to 223.255.255.255  
- Default Subnet Mask: 255.255.255.0 (/24)  
- Supports small networks  
- Used by small organizations and home networks  

---

### Class D:
- Range: 224.0.0.0 to 239.255.255.255  
- Used for multicast  
- Not used for host addressing  

---

### Class E:
- Range: 240.0.0.0 to 255.255.255.255  
- Reserved for experimental use  
- Not used in public networks  


## What is CIDR (Classless Inter-Domain Routing)?

- It is a method for representing an IP Range.  
- It is used to represent an IP range.  
- It is composed of an address in the range and a number between 0 and 32.  
- The number indicates the number of bits that are allocated to the address. The smaller the number - the larger the range.  

### CIDR Notation Example:
- 10.0.0.0/16 → 16 bits allocated for range  

 - 8 bits | 8 bits | 8 bits | 8 bits = 16 bits

- The IP address range 10.0.0.0 to 10.0.255.255 contains 65,536 usable IP addresses, as it represents a /16 CIDR block.  
- /16 Meaning: The "/16" indicates that the first 16 bits of the IP address are the network address, and the remaining 16 bits are for host addresses.  
- Calculation: With 16 bits for host addresses, there are 2^16 possible combinations, which equals 65,536.  

---

## What is Subnet?

- A subnet is a small piece of a large network. It is logical partition of an IP network.  
- Subnet is nothing but small network which we can get by subnetting.  
- It is a logical segment in the VNet.  
- Resources must be placed in a Subnet, cannot be placed directly in the VNet.  
- Resources in a subnet can talk to resources in other subnets in the same VNet.  
- Note: More good news: Azure usually shows the actual subnet range.  

---

## What is Subnet Mask?

Subnet mask is a 32-bit number used to differentiate the network component of an IP address by dividing the IP address into a network address and host address.  

---

## What is Subnetting?

Subnetting is the method for divide a large network into smaller sub-network of equal size.  

---

## What is Route Table?

In Azure, a route table is a set of rules that determines how network traffic is directed within a Virtual Network (VNet). It contains routes, which specify the destination IP address or CIDR block and where the traffic should be sent.  

---

## What is Route?

In Azure VNet, a "route" is a rule within a route table that determines where network traffic from a subnet or gateway is directed. We can create rule to define how network traffic flows, allowing you to control where packets are sent by specifying the destination IP range and the target.  

---

## What is Network Security Group (NSG)?
## What is Network Security Group (NSG)?

- A Network Security Group (NSG) is an Azure networking resource that contains a set of security rules used to allow or deny inbound and outbound network traffic to Azure resources.  
- NSGs can be associated with subnets or network interfaces (NICs) of virtual machines to control network access based on source, destination, port, protocol, and direction.  
- It is a gatekeeper for Subnets.  
- Defines who can connect in and out of subnet.  
- Think of it as a mini-firewall.  
- Protects subnet & NIC.   

### How NSG work:

Looks at 5 tuples:
- Source = Where did the connection come from  
- Source Port = The port the source is using  
- Destination = Where does the connection request goes  
- Destination Port = To which port does it want to connect  
- Protocol = TCP, UDP, OR Both  

Note: Based on these 5 tuples, the connection is either allowed or denied This is called Security Rule  

Each rule is assigned a number  
The lower the number – the higher the priority of the rule  

---

## What is Application Security Group (ASG)?

In Azure, an Application Security Group (ASG) is a network security feature that allows you to group virtual machines (VMs) logically based on their application tier or function, enabling you to define network security policies based on these groups rather than individual IP address.  
ASG allows us to group VMs logically and apply NSG rules using group names instead of IP addresses.  

---

## What is Firewall?

A firewall is a network security service that stands guard at the door of our network, protecting our resources from malicious internet traffic. It is used to monitor and control all incoming and outgoing traffic based on predefined rules. Azure Firewall is a centralized, fully managed firewall service that protects multiple VNets and resources.  

### Azure Firewall provides:
- Advanced filtering  
- Threat intelligence  
- Application rules  

---

## How to Access VM Securely?

Note: we have following option to securely access the VM.

## 1. JIT Access (Just In Time Access):

- Just-in-Time (JIT) VM access as a part of Microsoft Defender for Cloud.  
- It secures VMs by blocking management ports (such as RDP 3389, SSH 22) in Network Security Groups (NSGs) and only opens them on-demand for a set time, reducing attack surfaces.  
- Opens the port for access on demand, and automatically closes it.  
- Rest of the time – it’s closed.  
- Can be configured from the VM’s page in the portal.  
- Requires Security Center License Upgrade.  

---

## 2. VPN (Virtual Private Network):

- In Azure, “Azure VPN Gateway” is a VPN service which is a type of Virtual network Gateway.  
- Virtual Private Network (VPN) is a technology that establishes a secure, encrypted connection between devices over the internet.  
- Requires VPN software and license.  

---

## 3. Jump Box:

- Place another VM in the VNet.  
- Allow access ONLY to this VNet.  
- When need to access one of the other VMs – connect to this one and connect from it to the relevant VM.  
- Only one port is open (still kind of a problem…).  
- Cost: The additional VM (the Jump Box).  

## 4. Bastion:

A Bastion is a fully managed Platform as a Service (PaaS) that provides secure, seamless Remote Desktop Protocol (RDP) and Secure Shell (SSH) access to virtual machines (VMs) within a virtual network, without exposing the VMs to the public internet.

Using Bastion, 
- we can access Private VM within VNet.  
- A web-based connection to the VM  
- No open port is required  
- Simple and secure  

---

## Some Other Important Networking-related Cloud Services:

- Application Gateway  
- Load Balancer  
- Azure NAT Gateway  
- VNets Peering  
- Service Endpoint  
- Virtual Network Gateway  
- Private Endpoint  

---
