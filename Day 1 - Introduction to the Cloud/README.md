# Introduction to the Cloud #

# Before the cloud…

• If you needed a server, you had to:
• Buy physical servers
• Install operating systems and software
• Set up networking
• Maintain hardware
• Replace servers when they became old
• Hire a full IT team

And this was not just for servers, but also for:
•	Databases
•	Storage
•	User management
•	Security

Problems with this approach:
	Very expensive
	Time-consuming
	Wasted money when servers were idle
	Difficult to scale when users increased

# What is Cloud?
Compute, Networking, Storage and other services Managed by SOMEONE ELSE.
"The cloud" refers to a network of remote servers that store and manage data, run applications, and deliver content and services over the internet.
Instead of relying on our personal computer or local storage to handle everything, the cloud services, allowing users to access resources and data from anywhere at any time
with an internet connection. Such as Server, Network, Storage, Database, Application and services. In the cloud, we stop thinking about Infrastructure like Hardware and use
it as a Software.
Examples of Cloud services:
You already use cloud services every day:
•	Google Drive / Dropbox → Cloud Storage
•	Gmail / Outlook → Cloud Email
•	Netflix / Spotify → Cloud Streaming
•	Microsoft 365 / Adobe Creative Cloud → Cloud Software

# What is Cloud Computing?
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.

In other word:
Cloud computing is a combination of cloud and computing, where cloud refers to remote servers accessed over the internet, and computing refers to data processing, storage, and networking performed using those servers.
Note: In the cloud computing, the term “compute” describes the concepts and objects related to software Computation.

# Why do we need Cloud Computing?
Imagine hosting a website without cloud computing:
You would need to:
•	Buy expensive servers
•	Estimate how many users will visit
•	Handle traffic spikes
•	Hire people for monitoring and maintenance
•	Pay even when servers are not used

 Cloud solves all of this by providing:
•	Pay only for what you use
•	Automatic scaling
•	No hardware management
•	High availability

# What is Region?
Region = A geographic area where cloud data centers are located.
•	Each region is isolated from other regions
•	A region contains multiple Availability Zones
•	Example: East US, West Europe, Asia Pacific

# What is Availability zone (AZ)?
Each Region has multiple, Isolated locations known as availability zone (AZ).
•	A physically separate data center
•	Has its own power, cooling, and networking
•	Designed for high availability and fault tolerance
If one AZ fails, others continue working.

# Who Are Cloud Providers?
 
Cloud Providers are companies that:
•	Build huge data centers
•	Install servers, networking, cooling, electricity
•	Create cloud services
•	Make them accessible over the internet
Examples:
AWS (Amazon Web Services)
Microsoft Azure
Google Cloud Platform

In the cloud area… If you need a server, you can:

•	Create it in the cloud within minutes
•	Use it as you wish
•	Pay for what you use
•	Shut it down when not needed
•	Automatically maintained, patched, secured, monitored.

# Characteristics of Cloud Computing:
     
1. On-Demand Self Service:
•	It is the primary feature of the cloud provider by which we can create our account and use any services.
•	No human interaction is needed for resource provisioning.
•	Resource can be provisioned (created) with a click of a button.
•	Provisioning is available 24/7

2. Broad Network Access:
•	Resources can be accessed from anywhere at any time using the network
•	No physical access is required at any time.	

3. Resource Pooling:
•	It is a group of resource that can be assigned to user. In resource pooling, customers service run on shared physical hardware for the save of the cost.
•	Physical resources are shared between customers.
•	The cloud’s backbone decides which physical resource to allocate for a customer’s virtual services
•	Some advanced cloud services allow for physical resource separation.

4. Rapid Elasticity:
•	Resources can be scaled up and down as needed, automatically.
•	No need to purchase resources for a one-time peak scenario.
  
5. Pay-per-use Pricing:
•	Payment is done only for resources actually used. such as, Server time / DB storage / Function calls etc.
•	Payment method for cloud computing those charges based on uses.
•	Server time by the second.
•	No need to invest money in non-used resources.

6. Monitoring:
We can monitor our services and billing etc.

# Types of Clouds:

1. Public Cloud:
•	The Public cloud is a subscription base service that offered to any and all customers who want similar services.
•	The cloud is set up in the public network.
•	Managed by large companies.
•	Accessible through the internet.
•	Available to all clients and users.
•	Clients have no access to underlying infrastructure.

2. Private Cloud:
•	A cloud set up in an organization’s premises
•	Managed by the organization’s IT team
•	Accessible only in the organization’s network
•	Available to users from the organizations
•	Uses private cloud infrastructure and engines
•	Contains a subset of the public cloud’s capabilities

3. Hybrid Cloud:
It is a mixture of Public and Private Cloud. In Hybrid cloud, Application is running in a combination of different computing environment that share information to each other.

•	A cloud set up in an organization’s premises… but also connected to the public cloud.
•	Workload can be separated between the two clouds
•	i.e. Sensitive data in the organization’s premises, public data in the public cloud.
•	Usually managed by the public cloud, but not always.

4. Community Cloud:
• It refers to a shared cloud computing service environment that is targeted to a limited set of organization or employees. Such as Bank of head off trading firms. 


# Types of Cloud Services:

1. IaaS (Infrastructure as a Service):
• The cloud provides Provide the underlying platform:
  Compute
  Networking
  Storage
• The client handles, and is responsible for all the rest.  
    Most common example: Virtual Machines (Instances).
• The cloud provides the host machine, networking and disks.
• The client creates the virtual (guest) machine, installs software on it, patches it, maintains it etc.    

2. PaaS (Platform as a Service):
The cloud Providers provides platform for running apps:
•	Including: Compute, networking, storage, runtime environment, scaling, redundancy, security, updates, patching, maintenance etc.
•	The client just needs to bring the code to run.
    Most common example: (Azure: Web Apps), (AWS: Elastic Beanstalk)
•	The cloud Providers provides the runtime for running web application.
•	The client uploads the code, and it just runs.
•	The client has no access to the underlying virtual machines.


3. SaaS (Software as a Service):
   1. A software running completely in the cloud.
   2. The user doesn’t need to install anything on-premises or on his machine
   3. The providers of the software take care of updates, patches, redundancy, scalability etc.
