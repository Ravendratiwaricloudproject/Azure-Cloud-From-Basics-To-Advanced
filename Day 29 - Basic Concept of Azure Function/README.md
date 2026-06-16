# Day 29 – Basic Concepts of Azure Functions

## What is Azure Functions?

Azure Functions is a serverless compute service from Microsoft Azure that allows you to run small pieces of code without managing servers.

You simply write your code, and Azure automatically handles:

* Infrastructure
* Scaling
* Maintenance
* Availability

You only pay when your code runs.


# What are some good uses for Azure Functions?

Azure Functions are highly versatile and can be applied to a variety of scenarios. Here are some common and effective use cases:

1. Serverless APIs:
   
You can use Azure Functions to build RESTful APIs without managing infrastructure. Functions can handle HTTP requests, process data, and return responses, making it a cost-effective solution for API endpoints.

3. Data Processing:
   
Functions are ideal for processing data in real-time or in batch operations. This includes transforming, aggregating, or analyzing data.

Example:

• Real-Time Processing: Handle data streams or events from services like Azure Event Hubs or IoT Hub.
• Batch Processing: Execute periodic jobs for data cleanup, enrichment, or integration tasks.

3. Background Jobs:
   
Automate background tasks such as sending emails, generating reports, or performing scheduled maintenance.

Example:

• Timer Triggers: Schedule functions to run at specific intervals for routine tasks.


4. File Processing:
Azure Functions can process files uploaded to Azure Blob Storage, perform transformations, and move or archive files.

Example:
• Blob Triggers: Automatically process files when they are added or updated in blob storage.

5. Real-Time Notifications:
Create real-time notifications and alerts based on events from various sources, such as changes in databases or incoming messages.

Example:
• Event Grid Triggers: React to events from Azure Event Grid to send notifications or trigger actions.

6. Automation and Integration:

Automate workflows and integrate with other Azure services or third-party applications.

Example:
• Service Integration: Connect with services like Azure Logic Apps or Power Automate for complex workflows.
• Custom Integrations: Build custom integrations with APIs or external systems.

7. DevOps and CI/CD:
Implement serverless functions as part of your DevOps pipeline for automated deployment, testing, or monitoring tasks.

Example:

• Deployment Automation: Use functions to automate deployment tasks or trigger builds.
• Testing: Integrate functions into your testing pipeline to run tests or validations.


---

## What is Azure Function App?

An Azure Function App is a container or hosting environment for running one or more Azure Functions in the cloud. 

It provides:

* Runtime environment
* Configuration settings
* Authentication settings
* Monitoring and logging
* Scaling and deployment

### Important

A Function App can contain multiple functions, but all functions inside a Function App must use the same language runtime.

For example:

✅ Multiple python functions → Supported

❌ Node.js + Python functions in the same Function App → Not Supported



## What is the difference between Azure function app and Azure function?
The terms Azure Function and Azure Function App are closely related to each other, but they refer to different levels in the same service.

🔹 Azure Function: 
An Azure Function is a single unit of execution—basically one piece of serverless code that performs a specific task.
• It contains your actual logic (code). 
• It runs in response to a trigger.


🔹 Azure Function App:

An Azure Function App is a container (or hosting environment) for one or more Azure Functions.

• Function App groups multiple functions together.

• Shares configuration, runtime, scaling rules, and resources.


## What is Triggers and Bindings in Azure function?
In Azure Functions, triggers and bindings are core concepts that define how your function starts and how it interacts with other services.
Trigger?


### Trigger:

Trigger starts or invoke to a function.

Every Azure Function must have exactly one trigger.

Common triggers:

* HTTP Trigger
* Timer Trigger
* Queue Trigger
* Blob Trigger
* Event Grid Trigger
* Cosmos DB Trigger

### Binding:

A binding is a way to connect your function to other resources, such as databases, queues, or storage accounts etc.
Bindings can be:

• Input Bindings: Bring data into your function.
• Output Bindings: Send data from your function to an external service.

Example of Bindings:

Binding Type	 Direction	                   Description

Blob Storage	 Input                  	Reads a blob from Azure Blob Storage as input to the function
Queue Storage	 Output	                    Add a message to a storage queue
Cosmos DB	     Input	                    Read documents from a Cosmos DB
SendGrid	     Output	                    Send an email after function runs


# What is “Cold Start” in Azure Function:
A cold start in Azure Functions refers to the latency or delay that occurs when a function is invoked for the first time or after it has been idle for a while. This happens because the Azure platform needs to allocate resources, such as provisioning the compute environment, loading the function code, and setting up any necessary dependencies before executing the function.

• Cold starts basically occur in serverless architectures like Azure Functions when the function is deployed to a consumption plan, where resources are dynamically allocated based on demand.
 
• Azure Functions are completely managed by Azure
• After some time of inactivity Azure might take down the Function’s host
• The next activation of the Function will take time
• 2-3 seconds before the code runs
• A problem mainly for HTTP-Triggered functions

# How to avoid cold start?

• Select the right hosting plan


## What is Serverless Computing?

Serverless computing is a cloud model where you can run your code without creating or managing servers.

Azure automatically:

* Allocates resources
* Scales up/down
* Handles updates

You focus only on writing code.

For example: Azure Functions is a serverless service in Azure that allows you to execute code in response to events such as an HTTP request, file upload, timer schedule, or queue message.

Note: "Serverless doesn't mean there are no servers. It simply means Microsoft manages the servers for you. You write the code, Azure runs it when needed, automatically scales it, and you only pay when your code executes. This is exactly how Azure Functions work."



---


## Why Does Azure Functions Need a Storage Account?

Azure Functions uses a Storage Account to:

* Manage triggers
* Store logs
* Maintain execution state
* Enable scaling


# What Languages Does Azure Functions Support?

Azure Functions supports a variety of programming languages, allowing developers to use the language they are most comfortable with or best suited for their application. As of now, the supported languages include:
1.	.NET
2.	Node.js
3.	Java
4.	Python
5.	PowerShell Core
6.	Custom Handlers

# What is Durable Functions?
Durable Functions is an extension of Azure Functions that lets you write stateful workflows in a serverless way.
Normally, Azure Functions are stateless (each execution forgets everything). however, Durable Functions adds the ability to remember state, coordinate steps,
and run long workflows reliably.
With Durable Functions, you can:
•	Chain multiple functions together
•	Maintain state between steps
•	Handle long-running processes (minutes, hours, even days)
•	Automatically retry failed steps
•	Wait for external events (like user input or approvals)


# What is the difference between Azure Function, Logic App and Webjobs in Azure?

🔹Azure Functions:
Azure Functions is a serverless compute service that runs small pieces of code when triggered by an event.
You do not need to manage servers. It runs only when triggered and scales automatically.
Best for:
•	Event-driven tasks
•	APIs
•	Background processing
•	Microservices
Simple example: Like an electric switch — the light turns on only when you press it.

🔹Azure Logic Apps:
Azure Logic Apps is a serverless workflow automation service that allows you to connect applications and services with minimal or no code.
It provides a visual designer and many built-in connectors (Microsoft services, SaaS apps, databases, etc.).
Best for:
•	Business process automation
•	System integrations
•	Connecting multiple services without writing much code
•	Very useful for integrations between apps.
Simple example: Like a remote control — it connects and manages different devices easily.

🔹Azure WebJobs:
Azure WebJobs is a feature of Azure App Service that allows you to run background tasks inside a web app.
It runs as part of an App Service plan and does not scale independently. It is older compared to Azure Functions.
Best for:
•	Continuous background jobs
•	Scheduled tasks
•	Applications already running on App Service

Simple example: Like a fan running in your house — it keeps running in the background.


✅ Short note on when to choose what:
•	Azure Functions → When you need to write custom code that runs on demand and scales automatically.
•	WebJobs → When you already have an App Service and need background processing.
•	Logic Apps → When you need to connect multiple systems or automate workflows with minimal coding.

# Azure Functions hosting options:
When you create a function app in Azure, you must choose a hosting option for your app. these hosting options determine how your app scales, resources available per instance, and pricing.
Azure provides the following hosting options for your function code:

1. Flex Consumption

2. Functions Premium

3. App service

4. Container Apps Environment

5. Consumption (Windows)


#############################################################################################################################################################

# What is Azure Communication Services (ACS)?

ACS is a Microsoft communication platform that enables SMS, voice, video, chat, and email integration into applications.

# What is Azure Email Communication Service (ECS)?

It is a managed cloud service that enables applications to send transactional and marketing emails at scale. It's part of the Azure Communication Services family but focuses exclusively on email delivery.
Key capabilities:
•	Custom domain support (you can send from your own domain, e.g., noreply@yourdomain.com)
•	Azure Managed Domains for quick setup (e.g., noreply @azurecomm.net)
•	High-volume transactional email (OTP codes, notifications, receipts, alerts)
•	Delivery tracking and reporting



# Difference Between Azure Email Communication Service and Azure Communication Service?

In short: 

Communication Service is the broader platform for building real-time, multi-channel communication experiences (calls, video, chat, SMS).

Email Communication Service is a specialized service within that ecosystem focused purely on email delivery.

They can work together — you connect an Email Communication Service resource to a Communication Services resource to add email capability to your broader communication solution.




