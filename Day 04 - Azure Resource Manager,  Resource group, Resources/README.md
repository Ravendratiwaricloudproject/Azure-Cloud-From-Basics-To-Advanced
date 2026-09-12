# Azure Resource Manager (ARM)

 ARM is the deployment and management service for Azure. It provides a management layer that helps to create, update, and delete resources in our Azure account. we use management features like access control, locks, and tags to secure and organize our resources after deployment.

Key Features:

Template-Based Deployment: Use JSON templates to define and deploy resources consistently.

Dependency Management: ARM handles dependencies automatically, deploying resources in the correct order.

Rollback: Automatically revert or update deployments if something goes wrong.

Tagging: Organize resources for easier management.

# What are Azure Resource Manager(ARM) templates?

Azure Resource Manager templates are JavaScript Object Notation (JSON) files that define the infrastructure and configuration to deploy Azure resources.

ARM templates is Declarative language.


# Resource Groups
Resource Group is a Logical containers inside the subscription where we deploy and manage Azure resources like virtual machines, databases, web apps, and storage accounts.

Simplified: Resource groups are basically a grouping of resources together for easier management.

Why it matters: Makes it easier to organize, monitor, and control access to related resources.

# Resources
Think of resources in Azure as individual pieces or instances of the services you use. each Azure resource serves a specific purpose, such as storing data, running applications, or managing networks.

For the example:

virtual machines, app services, storage accounts, SQL databases, function apps, etc. all these are azure services,
And what you create using these services is called resources.
