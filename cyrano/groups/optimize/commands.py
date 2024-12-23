import asyncio
import logging
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory
from ...common.config import GLOBAL_CONFIG


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

    chat_completion_service = AzureChatCompletion(
        deployment_name=GLOBAL_CONFIG.get('azure_openai', 'deployment'),
        endpoint=GLOBAL_CONFIG.get('azure_openai', 'endpoint'),
        api_key=GLOBAL_CONFIG.get('azure_openai', 'api_key'))

    request_settings = AzureChatPromptExecutionSettings(
        max_tokens=1000,
    )

    system_message = """
    You are an assistant that helps people find the best
    3 experiences based on the job requirements. The user
    will provide you with a list of experiences and a list
    of requirements.
    """

    user_input = f"Requirements: {requirements}\n\n" \
                 f"Experiences: {experiences}"

    chat_history = ChatHistory(system_message=system_message)
    chat_history.add_user_message(user_input)

    response = await chat_completion_service.get_chat_message_content(
        chat_history=chat_history,
        settings=request_settings,
    )
    if response:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(response)
