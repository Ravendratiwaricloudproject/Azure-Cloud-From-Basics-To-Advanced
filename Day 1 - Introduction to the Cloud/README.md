# Introduction to the Cloud #

# Before the cloud…
If you needed a server, you had to:
1. Buy physical servers
2. Install operating systems and software
3. Set up networking
4.  Maintain hardware
5.   Replace servers when they became old
6.   Hire a full IT team

And this was not just for servers, but also for:
1. Databases
2. Storage
3. User management
4. Security

Problems with this approach:
1. Very expensive
2. Time-consuming
3. Wasted money when servers were idle
4. Difficult to scale when users increased

# What is Cloud?
Compute, Networking, Storage and other services Managed by SOMEONE ELSE.The cloud refers to a network of remote servers that store and manage data, run applications, and deliver content and services over the internet.
Instead of relying on our personal computer or local storage to handle everything, the cloud services, allowing users to access resources and data from anywhere at any time
with an internet connection. Such as Server, Network, Storage, Database, Application and services. In the cloud, we stop thinking about Infrastructure like Hardware and use
it as a Software.
Examples of Cloud services:
You already use cloud services every day:
1. Google Drive / Dropbox → Cloud Storage
2. Gmail / Outlook → Cloud Email
3. Netflix / Spotify → Cloud Streaming
4. Microsoft 365 / Adobe Creative Cloud → Cloud Software

# What is Cloud Computing?
Cloud computing is the on-demand delivery of IT resources over the Internet with pay-as-you-go pricing.

In other word:
Cloud computing is a combination of cloud and computing, where cloud refers to remote servers accessed over the internet, and computing refers to data processing, storage, and networking performed using those servers.
Note: In the cloud computing, the term “compute” describes the concepts and objects related to software Computation.

# Why do we need Cloud Computing?
Imagine hosting a website without cloud computing:
You would need to:
1. Buy expensive servers
2. Estimate how many users will visit
3. Handle traffic spikes
4. Hire people for monitoring and maintenance
5. Pay even when servers are not used

 Cloud solves all of this by providing:
 1. Pay only for what you use
 2. Automatic scaling
 3. No hardware management
 4. High availability

# What is Region?
Region = A geographic area where cloud data centers are located.
1. Each region is isolated from other regions
2. A region contains multiple Availability Zones
3. Example: East US, West Europe, Asia Pacific

# What is Availability zone (AZ)?
Each Region has multiple, Isolated locations known as availability zone (AZ).
1. A physically separate data center
2. Has its own power, cooling, and networking
3. Designed for high availability and fault tolerance
If one AZ fails, others continue working.

# Who Are Cloud Providers?
 Cloud Providers are companies that:
 1. Build huge data centers
 2. Install servers, networking, cooling, electricity
 3. Create cloud services
 4. Make them accessible over the internet
Examples:
AWS (Amazon Web Services)
Microsoft Azure
Google Cloud Platform

In the cloud area… If you need a server, you can:
1. Create it in the cloud within minutes
2. Use it as you wish
3. Pay for what you use
4. Shut it down when not needed
5. Automatically maintained, patched, secured, monitored.

# Characteristics of Cloud Computing:
1. On-Demand Self Service:
   It is the primary feature of the cloud provider by which we can create our account and use any services.
   No human interaction is needed for resource provisioning.
   Resource can be provisioned (created) with a click of a button.
   Provisioning is available 24/7

2. Broad Network Access:
   Resources can be accessed from anywhere at any time using the network
    No physical access is required at any time.	

3. Resource Pooling:
   It is a group of resource that can be assigned to user. In resource pooling, customers service run on shared physical hardware for the save of the cost.
   Physical resources are shared between customers.
   The cloud’s backbone decides which physical resource to allocate for a customer’s virtual services
   Some advanced cloud services allow for physical resource separation.

4. Rapid Elasticity:
   Resources can be scaled up and down as needed, automatically.
   No need to purchase resources for a one-time peak scenario.
  
5. Pay-per-use Pricing:
   Payment is done only for resources actually used. such as, Server time / DB storage / Function calls etc.
   Payment method for cloud computing those charges based on uses.
   Server time by the second.
   No need to invest money in non-used resources.

6. Monitoring:
   We can monitor our services and billing etc.

# Types of Clouds:

1. Public Cloud: The Public cloud is a subscription base service that offered to any and all customers who want similar services. The cloud is set up in the public network and Managed by large companies. it is Accessible through the internet and Available to all clients and users. However, Clients have no access to underlying infrastructure.

3. Private Cloud:
   A cloud set up in an organization’s premises and Managed by the organization’s IT team. private cloud is Accessible only in the organization’s network and Available to users from the organizations.

4. Hybrid Cloud: It is a mixture of Public and Private Cloud. In Hybrid cloud, Application is running in a combination of different computing environment that share information to each other. Hybrid Cloud set up in an organization’s premises… but also connected to the public cloud. Workload can be separated between the two clouds
    i.e. Sensitive data in the organization’s premises, public data in the public cloud.
   Usually managed by the public cloud, but not always.

6. Community Cloud:
   It refers to a shared cloud computing service environment that is targeted to a limited set of organization or employees. Such as Bank of head off trading firms. 


# Types of Cloud Services:
1. IaaS (Infrastructure as a Service):
   The cloud provider provides the underlying infrastructure, including: Compute, Networking, Storage.


   The client is responsible for:
   
   Operating System
   Middleware
   Runtime
   Applications
   Data
   Most common example: Virtual Machines (VMs / Instances)
   
3. PaaS (Platform as a Service):
   The cloud provider provides a platform for running applications, including: Compute. Networking, Storage, Runtime environment, Scaling, Redundancy, Security, Updates, patching, and maintenance.
   
   The client only needs to bring the application code.
   
   Most common examples:
   Azure: Web Apps (Azure App Service)
   AWS: Elastic Beanstalk
   In PaaS:
   The cloud provider manages the runtime and infrastructure required to run the web application.
   The client uploads the code, and the application runs automatically.
   The client does not have access to the underlying virtual machines.


5. SaaS (Software as a Service): A software application that runs completely in the cloud. The user does not need to install anything on-premises or on their local machine. The software provider takes care of updates, patches, scalability, redundancy, security, and maintenance.

   Common SaaS examples:
   Microsoft 365
   Salesforce
