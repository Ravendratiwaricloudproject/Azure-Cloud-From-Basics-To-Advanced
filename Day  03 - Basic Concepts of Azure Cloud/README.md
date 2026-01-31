# Management Levels and Hierarchy in Azure.

1. Management Groups

Purpose: Help you manage access, policy, and compliance for multiple subscriptions.

Key Point: All subscriptions within a management group automatically inherit the conditions applied to that group.

Use Case: Great for organizations with many subscriptions—it lets you apply policies at scale instead of individually.

2. Subscriptions

Definition: A subscription logically associates user accounts with the resources they create.

Key Points:

Each subscription has limits or quotas on the number of resources it can use.

Organizations use subscriptions to manage costs and allocate resources for users, teams, or projects.

Tip: Think of subscriptions as containers that help to organize billing and usage.

3. Resource Groups

Definition: Logical containers where you deploy and manage Azure resources like virtual machines, databases, web apps, and storage accounts.

Simplified: Resource groups are basically a grouping of resources for easier management.

Why it matters: Makes it easier to organize, monitor, and control access to related resources.

4. Resources

Definition: The building blocks of your Azure environment.

Examples: Virtual machines, databases, storage accounts, networking services, and more.

Key Point: Each resource is provisioned and managed individually, even if it's part of a resource group.

5. Azure Resource Manager (ARM)

Definition: ARM is the deployment and management service for Azure. It provides a consistent way to manage resources.

Key Features:

Template-Based Deployment: Use JSON templates to define and deploy resources consistently.

Dependency Management: ARM handles dependencies automatically, deploying resources in the correct order.

Rollback/Roll-forward: Automatically revert or update deployments if something goes wrong.

Tagging & Categorization: Organize resources for easier management.

Note: Understanding ARM, resources, and resource groups is fundamental to managing Azure efficiently.

6. Difference Between Subscriptions and Azure Accounts
  
Subscriptions:
1. It is a Logical Container.
2. Contains the various resources you provision in the cloud (VMs, databases, networks, etc.)
3. Can be attached to multiple Azure accounts

 Azure Accounts:
 1. It is An identity with access to resources in the subscriptions (i.e., you)
 2. Can be attached to multiple subscriptions
