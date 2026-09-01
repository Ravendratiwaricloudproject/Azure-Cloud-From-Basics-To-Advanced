# Day-3: Basic Concepts of Azure Cloud

## What is Azure/Microsoft Azure?

Microsoft Azure is a public cloud computing platform that provides on-demand IT services such as compute, storage, networking, databases, and security over the internet.

It allows individuals and companies to use computing power, storage, databases, and other IT services over the internet without having to purchase or maintain physical hardware. You only pay for the specific services that you use.

Microsoft's Azure offering more than 200 products and services across a global network of datacenters. It allows individuals and organizations to build, deploy, and manage applications and services through Microsoft-managed data centers around the world.

It reduces the time and cost of maintaining on-premises hardware and provides a unified cloud computing environment where AI, data, services, and applications can work together.

## What is an Azure Account?
An Azure Account is the sign-in identity, typically a Microsoft Entra ID account.
It is the identity used to access and manage Azure resources.

## What is a Tenant?

A tenant is a dedicated and isolated instance of the Microsoft Entra ID service that an organization receives when it signs up for a Microsoft cloud service such as Azure, Microsoft 365. Each tenant has its own identity and access management scope, and is distinct and separate from other tenants. A tenant is also associated with a unique tenant ID, which is a globally unique identifier (GUID) that identifies the tenant in Microsoft Entra ID.

---

## What is a Directory?

A directory is a container for objects such as users, groups, and applications, Service Principals and it is used to manage access to resources in Azure. A directory is also associated with a unique directory ID, which is a GUID that identifies the directory in Microsoft Entra ID.

## Difference between Tenant and Directory:
 The main difference between a tenant and a directory is that a tenant is a dedicated and isolated instance of Azure Entra ID, while a directory is a container for objects such as users, groups, and applications. Every tenant has exactly one directory, and every directory belongs to exactly one tenant.

 # Does Tenant ID (GUID) and Directory ID (GUID) are the same value?
 
 Yes, Tenant ID and Directory ID are the same value — they are two names for the same GUID. Microsoft just exposes it under both names depending on the context:

Tenant ID — used when talking about authentication, subscriptions, and service access

Directory ID — used when talking about identity objects (users, groups, apps)

## What are Azure Management Groups?

A **Management Group** is an organizational layer above subscriptions. Use it to apply **Azure Policy** and **RBAC** across many subscriptions in one shot.

A Management Group is a container that holds multiple Azure subscriptions together so you can manage them as one unit. Instead of setting policies and access rules on each subscription separately, you set them **once on the Management Group** — and they automatically apply to all subscriptions inside it. This is called **inheritance.**

**Example:**
Apply a policy on Finance MG that says "only create VMs in India region" ? every subscription inside Finance MG follows this rule automatically.

All subscriptions within a Management Group must trust the same **Microsoft Entra tenant.**

---

## Root Management Group

The **Root Management Group** is the top-level management group that Azure automatically creates for every tenant. You do not create it — it is always there.

Every Management Group and subscription in your tenant sits inside the Root MG. Any policy or access rule set here applies to your **entire organization.**

---

## What is a Subscription?

A **Subscription** is the billing and authorization boundary in Azure. It answers the question: **"Where is the bill and who can access what?"**

- All resources live inside a subscription
- It defines **who can do what** (RBAC inherited from the directory)
- It defines **where charges roll up** (billing)
- It enforces **quotas and limits**
- A subscription is linked to exactly one tenant at a time.
- A subscription is linked to exactly one directory at a time.
- Many subscriptions can belong to one tenant, but one subscription cannot belong to multiple tenants simultaneously.
- We can move a subscription to a different tenant, but at any point in time it remains tied to exactly one.

What is preserved after transfer:

All resources inside the subscription (VMs, storage, databases, etc.)

The subscription ID

What is lost or reset after transfer:

All RBAC role assignments — must be manually reassigned

Managed identities — system-assigned are deleted; user-assigned must be relinked

Azure AD-integrated services may break temporarily and need reconfiguration

## What is a Resource Group?

A Resource Group is a logical container inside a subscription that groups related resources together. It answers the question: How do I group related things I deploy together?
- Every resource must belong to exactly **one** resource group
- Resources in a resource group typically share the same lifecycle (deployed, updated, and deleted together)
- A resource group belongs to one subscription only.

## What is a Resource?

Actual Azure service — VM, Database, Storage etc.

## Quick Reference Table

- Tenant:  Your company's identity boundary in Microsoft Entra ID

- Directory: Stores users, groups, apps — answers "Who are you?

- Azure Account: Sign-in identity — how a person authenticates

- Management Group: Groups subscriptions to apply policies in one shot

- Root Management Group: Top-level MG auto-created by Azure — holds everything

- Subscription: Billing and access boundary — holds all resources

- Resource Group: Logical folder inside a subscription for related resources

- Resource:  Actual Azure service — VM, Database, Storage etc.
