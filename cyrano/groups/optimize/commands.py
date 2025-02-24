import asyncio
import logging
from cyrano.processes.resume_optimization_process import ResumeOptimizationProcess
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.kernel import Kernel
from semantic_kernel.processes.kernel_process.kernel_process_event import KernelProcessEvent
from semantic_kernel.processes.local_runtime.local_kernel_process import start
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

    asyncio.run(_optimize_experiences_sk(experiences_file, requirements_file, output_file))


async def _optimize_experiences_sk(experiences_file: str,
                                   requirements_file: str,
                                   output_file: str) -> None:
    logging.info('Optimize experiences with Semantic Kernel')

    kernel = Kernel()

    chat_completion_service = AzureChatCompletion(
        service_id='azure_chat_completion',
        deployment_name=GLOBAL_CONFIG.get('azure_openai', 'deployment'),
        endpoint=GLOBAL_CONFIG.get('azure_openai', 'endpoint'),
        api_key=GLOBAL_CONFIG.get('azure_openai', 'api_key'))

    kernel.add_service(chat_completion_service)

    kernel_process = ResumeOptimizationProcess.create_process().build()

    await start(
        kernel_process,
        kernel,
        KernelProcessEvent(id=ResumeOptimizationProcess.ProcessEvents.OptimizeResumeEvent,
                           data={
                               'experiences_file': experiences_file,
                               'requirements_file': requirements_file,
                               'output_file': output_file
                           }),
    )
