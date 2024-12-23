# Usage

To use Cyrano to improve your resume:

1. Create a file that lists, in a Markdown format, the experiences you want to filter
1. Create a file containing the job requirements
1. Call Cyrano:

    ```powershell
    cyrano optimize experiences `
        --experiences-file .\experiences.md `
        --requirements-file .\acme-ai-architect.txt `
        --output-file .\acme-ai-architect-experiences.md
    ```

The file `acme-ai-architect-experiences.md` then contains the best 3 experiences.
