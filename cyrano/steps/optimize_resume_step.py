from enum import Enum
from semantic_kernel import Kernel
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from semantic_kernel.processes.kernel_process.kernel_process_step import KernelProcessStep
from semantic_kernel.processes.kernel_process.kernel_process_step_context import KernelProcessStepContext
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.contents import ChatHistory


class OptimizeResumeStep(KernelProcessStep):

    class OutputEvents(Enum):
        ResumeOptimized = 'ResumeOptimized'

    @kernel_function
    async def run(self,
                  context: "KernelProcessStepContext",
                  data: "dict",
                  kernel: "Kernel") -> None:
        """
        Optimize the resume based on the job requirements and
        save the results in the output file.
        """

        experiences = data["experiences"]
        requirements = data["requirements"]

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

        azure_chat_completion = kernel.get_service('azure_chat_completion')
        response = await azure_chat_completion.get_chat_message_content(
            chat_history=chat_history,
            settings=request_settings,
        )
        optimization = response.content if response else None

        await context.emit_event(process_event=OptimizeResumeStep.OutputEvents.ResumeOptimized,
                                 data={
                                     'optimization': optimization
                                 })
