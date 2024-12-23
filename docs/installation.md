# Installation

1. Create the Python virtual environment:

    ```Powershell
    python -m venv env

    .\env\Scripts\Activate.ps1
    ```

1. Install the dependencies and application:

    ```Powershell
    python -m pip install -r requirements.txt
    python -m pip install -e .
    ```

1. Verify that application was successfully installed:

    ```Powershell
    > cyrano -h

    Group
        cyrano

    Subgroups:
        optimize : Commands for optimizing resumes.
    ```

## Configuration

1. Log into [Azure AI Foundry](https://oai.azure.com):
    1. create a project
    1. deploy a model

1. Update the `~/.cyrano/config` file with the Azure OpenAI values:

    ```text
    [azure_openai]
    deployment = [name of the deployed model]
    endpoint = [AI Foundry project endpoint]
    api_key = [AI Foundry project api key]
    ```
