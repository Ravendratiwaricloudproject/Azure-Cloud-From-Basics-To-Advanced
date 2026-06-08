# Steps to create and deploy Azure Function.

# Prerequisites:

- Download and install Python 3.12:
  https://www.python.org/downloads/windows/

- Download and install Azure CLI:
  https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-windows?view=azure-cli-latest&pivots=winget

- Download and install VS Code:
  https://code.visualstudio.com/download

- Download and install azure function Core Tools:
  https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=windows%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-python

# Open you VS Code and install following Extensions:

- Azure CLI Tools → Run Azure CLI to log in to Azure portal and interact with Azure resources, and create and manage resources    from VS Code

 Check the version- az --version

- Azure Functions → Build & deploy functions

  * Check the version: func --version

- Azure Resources → Manage Azure login & resources

- Python → Python language support

  * Check the version: python3 --version

- Pylance → Advanced Python IntelliSense and type checking

- Note: Make sure you install all the extensions provided by Microsoft.
##################################################################################################################################

# Option-1: Go back to VS code and create Azure function locally with Event Grid trigger:
  
  1. Create one Folder with any name in you Local PC.

  2. Search for VS code in your Local PC and open it. In Visual Studio Code, press "fn + F1" OR you can press "ctrl + shift + p" to open the command palette,  enter and select Azure Functions: Create new project.

  4. For your project workspace, select a directory Name and location. Make sure that you either create a new folder or choose an empty folder for the project workspace.

  - Don't choose a project folder that's already part of a workspace.

  4. At the prompts, provide the following information:

     - Select a language: Select Python

     - Select a Python programming model:	Select Model V2

     - Select a Python interpreter to create a virtual environment. Select your preferred Python interpreter. If an option isn't  shown, enter the full path to your Python binary.

     - Select a template for your project's first function: EventGrid Trigger

     - Provide a function name: EX.	Enter EventGridBlobTrigger.

     - Select a workspace window: Open in current window

  5. Once we create the function locally, it will generate the following files:

       1. local.settings.json

       2. host.json

       3. function.py

       4. requirements.txt

      - Go inside the folder:

        * cd FolderName

     - Check all these files in the current GitHub repository and update your file accordingly.

# Option-2

- Step-1: Clone the Day 29 - Azure Function GitHub repository

  * git clone ....

- Note: Make sure that you have downloaded and installed the git in you PC.

- Step-2: Open the Github repository in you VS code.

- Step-3: Review the code in each file and if you want you can change the function name in your function.py file:

  * Current function name: EventGridBlobTrigger

- Step-4: create a virtual environment for python base azure function.

  * For Windows OS:

    Open Terminal → New Terminal in VS code and run following commands:

     1. install the venv module: python -m venv .venv

     2. Activate it: 
     
     run: .venv\Scripts\Activate.ps1

  * For Linux:

     1. install the venv module first. Run: sudo apt install python3-venv -y
    
     2. Then proceed with:

        bashpython3 -m venv .venv

       source .venv/bin/activate

  - Step-5: Install the folling Python packages listed in the requirements.txt file.

          *  azure-functions

          *  azure-communication-email

          1. Go to function app folder and run following command base on the OS:

             * For Linux: pip install -r requirements.txt

             * For Windows:

               py -m pip install -r requirements.txt

               python -m pip install -r requirements.txt

  - Step-6: - Login to Azure portal and Create Resource Group and Function App, Azure Email Communication Service and Azure Communication Service.

  - Step-7: Create Azure storage account with container for testing.

  - Step-8:  Create EventGrid Subscription for storage account.

  - Step-9: Go to Azure Portal → Function App → setting → Environment variable →  App Settings and add environment variables:
          
          * ACS_CONNECTION_STRING: Value of the Azure communication service connection string.

          * ACS_SENDER_ADDRESS: value of the Azure Email communication service sender address.

          * TO_EMAIL: Value of the email where we want to send notification.

  - Step-10: Go to the test storage account and upload any file to the container to verify that the Event Grid triggers the Azure Function, and that the Azure Function invokes ACS to send an email notification.
  
  - Note: Team you can upload any file name such as-  .txt, .jpg, .pdf, anything.

  # Now open your Email and check if you received notification.

     

  

