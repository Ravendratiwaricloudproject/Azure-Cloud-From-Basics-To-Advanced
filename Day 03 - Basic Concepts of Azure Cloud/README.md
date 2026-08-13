# Day-3: Basic Concepts of Azure Cloud

## What is Azure/Microsoft Azure?

Microsoft Azure is Microsoft's public cloud computing platform that provides on-demand IT services such as compute, storage, networking, databases, and security over the internet.

It allows individuals and companies to use computing power, storage, databases, and other IT services over the internet without having to purchase or maintain physical hardware. You only pay for the specific services that you use.

Microsoft's Azure offering more than 200 products and services across a global network of datacenters. It allows individuals and organizations to build, deploy, and manage applications and services through Microsoft-managed data centers around the world.

It reduces the time and cost of maintaining on-premises hardware, and provides a unified approach to cloud computing with AI, data, and application services all working together.

## What is an Azure Account?

An **Azure Account** is the sign-in identity (Microsoft Entra ID account). It is how a person authenticates into Azure.

It does not contain resources by itself — it is simply the identity used to access and manage resources across subscriptions.


## What is a Tenant?

A **Tenant** is a dedicated instance of **Microsoft Entra ID** that your organization gets when it signs up for any Microsoft cloud service (Azure, Microsoft 365, etc.).

Think of it as your **company's identity boundary** — it holds all your users, groups, and applications in one place. Every Azure subscription must be linked to exactly one tenant.

---

## What is a Directory?

A **Directory** (Microsoft Entra ID) is the identity store inside a tenant. It answers the question: **"Who are you?"**

It contains:
- Users
- Groups
- Applications
- Service Principals

Every tenant has exactly one directory, and the directory is responsible for authentication and identity management.


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

A subscription is linked to exactly **one directory** at a time, but you can transfer a subscription to a different directory if needed.

---

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
