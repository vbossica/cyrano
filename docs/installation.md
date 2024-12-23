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

1. Update the `~/.cyrano/config` file with the Azure OpenAI values:

    ```text
    [azure_openai]
    deployment =
    endpoint =
    api_key =
    ```
