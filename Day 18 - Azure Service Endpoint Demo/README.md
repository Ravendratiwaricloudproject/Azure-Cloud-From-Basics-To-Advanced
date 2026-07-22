# Introduction to Azure Service Endpoints

# What is Service Endpoint?

Azure Service Endpoints are a networking feature in Microsoft Azure that allows you to securely connect your Virtual Network (VNet) to supported Azure services. when you enable service endpoints on a virtual network, they extend the private IP address space of that virtual network to the Azure service over the Azure backbone network.

Service Endpoints provide a direct and secure connection to Azure services such as Azure Storage, Azure SQL Database, and Azure Key Vault without requiring traffic to traverse the public internet.

- Note: In AWS, the equivalent of Azure's “Service Endpoint” is "Gateway VPC Endpoint"

- Key Characteristics of Service Endpoints:

• Public Service, Private Routing: Service endpoints route traffic through the Azure backbone network while still accessing Azure services using their public IP addresses. The traffic does not traverse the public internet.

• Network Security Group (NSG) Integration: Service endpoints work with Network Security Groups (NSGs), allowing you to control outbound traffic from subnets to Azure services.

• DNS Resolution: Service endpoints continue to use the public DNS name of the Azure service (for example, storageaccount.blob.core.windows.net). DNS resolution remains public, but the network path stays within the Azure backbone. 

- Azure Services That Support Service Endpoints:

• Azure Storage

• Azure SQL Database

• Azure Synapse Analytics

• Azure Database for PostgreSQL

• Azure Database for MySQL

• Azure Cosmos DB

• Azure Key Vault

• Azure Service Bus

• Azure Event Hubs

• Azure App Service

• Azure AI Services

• And many more.


- When to Use Service Endpoints:

Choose Service Endpoints if:

• You want to connect to Azure services like Storage, SQL, or Key Vault using the Azure backbone network.

• Your security requirements do not mandate complete isolation from the public internet.

• You need to leverage Network Security Groups (NSGs) to limit access from specific subnets or VNets.


- Important Note:

A Service Endpoint allows an Azure resource inside a VNet (for example, a VM) to securely access an Azure PaaS service (for example, Storage Account).

Azure service endpoints cannot be directly used for traffic originating from an on-premises network. 

Service endpoints are designed to secure Azure service resources to specific virtual networks within Azure, not for connecting from on-premises. If you need to access Azure resources from your on-premises network, you'll need to use other methods like ExpressRoute or VPN.

By default, Azure service resources secured to virtual networks aren't reachable from on-premises networks. If you want to allow traffic from on-premises, you must also allow public (typically, NAT) IP addresses from your on-premises or ExpressRoute.
