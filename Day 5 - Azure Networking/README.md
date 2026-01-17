# What is Virtual Networks(VNets)?

•	It is a Virtual network or Data center inside Azure for one client. it is logically Isolated from other virtual networks

•	it is a network in which you can deploy cloud resources

•	Many cloud resources are deployed within Vnets Ex. VMs, App Services, DBs, etc.

•	Think of it as your organization’s private network

•	In AWS it’s called VPC – Virtual Private Cloud Other organizations’ VNets

•	Resources in VNet can communicate with each other by default but not with resources in other VNets

•	To establish connection between two VNet, we can use Vnet peering.

Characteristics of VNets:
• Scoped to a single Region

• Cannot span multiple Regions

• Scoped to a single Subscription

• Can be connected two VNets via Peering

• Segmented using Subnets

• Protected using NSG (on the Subnets)

Addresses of VNets:
• Each VNet has its own IP address range

• By default – 65,536 addresses

• Can be customized

• All network devices must be in this address range

• Expressed using CIDR Notation

• cannot peer two VNets that have overlapping or identical IP address spaces including subnets. As this will lead to address conflicts and routing issues.

# What is Addressing?
Addressing is the method used in computer networking to identify and locate devices so that data can be sent to the
correct destination.

In simple terms, addressing tells the network:
Who is sending the data
Who should receive the data

Why Addressing is Important:
Devices wouldn’t know where to send data
Data could reach the wrong device
Communication over a network wouldn’t work

Without addressing:
Devices wouldn’t know where to send data
Data could reach the wrong device
Communication over a network wouldn’t work

Types of Addressing:
1. Physical Addressing: It is a MAC Address (48 bits)
2. Logical Addressing: It is a IP Address

# What is IP (Internet protocol)?
• IP is a Logical address comprises of ‘4’ octet and each octet is differentiated by dot (.)

• IP address is used to provide communication between device over the internet.

Types of IP Address:
1. IPv4 (32 bits)
2. IPv6 (128 bits)

Types of IPv4 Address:

(1) Private IP  Address

• It is work at LAN

• It is used to communicate within the same network

• It is available free of cost

• Private IP is secure

• It is required NAT to communicate with device on internet

• Private IP range: 
   10.0.0.0 – 10.255.255.255
   172.16.0.0 – 172.31.255.255
   192.168.0.0 – 192.168.255.255

(2) Public IP  Address

•	It is work at WAN

•	It is used to communicate outside the network

•	It is used to get internet service

•	It is not available free of cost

•	Public IP is not secure

•	It is not required NAT to communicate with device on internet

# Types of IP Address Class:
Class A: 1-126 (Large networks, first octet for network, remaining three for hosts)

Class B:	128-191 (Medium-sized networks, first two octets for network, remaining two for hosts)

Class C:	192-223 (Small networks, first three octets for network, last octet for hosts)

Class D:	224-239 (Multicast addressing, used to send data to multiple devices simultaneously)

Class E: 240-255 (Reserved for experimental purposes)

# What is Subnet?
A subnet is a small piece of a large network. It is logical partition of an IP network.
Subnet is nothing but small network which we can get by subnetting.
It is A logical segment in the VNet
Resources must be placed in a Subnet, cannot be placed directly in the VNet.
Resources in a subnet can talk to resources in other subnets in the same VNet

Note: More good news: Azure usually shows the actual subnet range

# What is Subnet Mask?
Subnet mask is a 32-bit number used to differentiate the network component of an IP address by dividing the IP address into a network address and host address.

# What is Subnetting?
Subnetting is the method for divide a large network into smaller sub-network of equal size.


# What is Route table?
In Azure, a route table is a set of rules that determines how network traffic is directed within a Virtual Network (VNet). It contains routes, which specify the destination IP address or CIDR block and where the traffic should be sent.

# What is Route?
In Azure VNet, a "route" is a rule within a route table that determines where network traffic from a subnet or gateway is directed.  We can create rule to define how network traffic flows, allowing you to control where packets are sent by specifying the destination IP range and the target.

# What is Network Security Group(NSG)?

•	It is a  gatekeeper for Subnets

•	Defines who can connect in and out of subnet

•	Think of it as a mini-firewall

•	Should be a standard part of Subnet creation

 How NSG work:
Looks at 5 tuples:

•	Source = Where did the connection come from

•	Source Port = The port that source is using

•	Destination = Where does the connection request goes

•	Destination Port = To which port does it want to connect

•	Protocol = TCP, UDP, OR  Both

Note:	Based on these 5 tuples the connection is either allowed or denied This is called Security Rule

•	Each rule is assigned a number

•	The lower the number – the higher the priority of the rule
 
NSG in VMs:

•	An NSG is automatically created and attached to every newly created VM’s network interface

•	By default – open RDP (on Windows) or SSH (on Linux) port to anyone we MUST be handled first thing after creation


# What is Application Security Group (ASG)?

In Azure, an Application Security Group (ASG) is a network security feature that allows you to group virtual machines (VMs) logically based on their application tier or function, enabling you to define network security policies based on these groups rather than individual IP addresses.

# What is Firewall?
A firewall is a network security service that stands guard at the door of our network, protecting our resources from malicious internet traffic. It is used to monitor and control all incoming and outgoing traffic based on predefined rules. 
 

# How to VM Access securely? 

Note: We have  following option to securely access the VM. 
 
1.	JIT Access(Just In Time Access):
   
•	Opens the port for access on demand, and automatically closes it

•	Rest of the time – it’s closed

•	Can be configured from the VM’s page in the portal

•	Requires Security Center License Upgrade

3. VPN (Virtual private network):
4. 
•	In Azure, “Azure VPN Gateway” is a VPN service which is a type of Virtual network Gateway.

•	A secure tunnel to the VNet

•	Can be configured so that no one else can connect to the VNet

•	Requires VPN software and license

6. Jump Box:
    
•	Place another VM in the VNet

•	Allow access ONLY to this VNet

•	When need to access one of the other VMs – connect to this one and connect from it to the relevant VM

•	Only one port is open (still kind of a problem…)

•	Cost: The additional VM (the Jump Box)

4.	Bastion:
   
•	A Bastion is a fully managed Platform as a Service (PaaS) that provides secure, seamless Remote Desktop Protocol (RDP) and Secure Shell (SSH) access to virtual machines (VMs) within a virtual network, without exposing the VMs to the public internet.

•	Using Bastion, we can access Private VM within VNet.

•	A web-based connection to the VM

•	No open port is required

•	Simple and secure



 

