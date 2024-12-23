import asyncio
import logging
from ...common.config import GLOBAL_CONFIG
from semantic_kernel import Kernel
from semantic_kernel.utils.logging import setup_logging
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)


def optimize_experiences(experiences_file: str,
                         requirements_file: str,
                         output_file: str) -> None:
    """
    Optimize the experiences based on the job requirements and
    save the results in the output file.

    :param experiences_file: the file containing the experiences
    :param requirements_file: the file containing the job requirements
    :param output_file: the output file
    """

    asyncio.run(_optimize_experiences(experiences_file, requirements_file, output_file))


async def _optimize_experiences(experiences_file: str,
                                requirements_file: str,
                                output_file: str) -> None:
    logging.info('Optimize experiences')

    # read experiences and job requirements
    with open(experiences_file, 'r', encoding='utf-8') as file:
        experiences = file.read()
    with open(requirements_file, 'r', encoding='utf-8') as file:
        requirements = file.read()

    kernel = Kernel()
    kernel.add_service(AzureChatCompletion(
        deployment_name="cyrano",
        endpoint=GLOBAL_CONFIG.get('openai', 'endpoint'),
        api_key=GLOBAL_CONFIG.get('openai', 'api_key')))

    setup_logging()
    logging.getLogger("kernel").setLevel(logging.DEBUG)

    prompt = f"Optimize the experiences based on the job requirements:\n" \
             f"Requirements: {requirements}\n" \
             f"Experiences: {experiences}"

    answer = await kernel.invoke_prompt(prompt)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(answer.encode('utf-8'))
