from enum import Enum
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from semantic_kernel.processes.kernel_process.kernel_process_step import KernelProcessStep
from semantic_kernel.processes.kernel_process.kernel_process_step_context import KernelProcessStepContext


class PublishResumeStep(KernelProcessStep):

    class OutputEvents(Enum):
        ResumePublished = 'ResumePublished'

    @kernel_function
    async def run(self,
                  context: KernelProcessStepContext,
                  data: dict) -> None:
        print("Publish resume step")

        with open('data/a.out', 'w', encoding='utf-8') as file:
            file.write(data['optimization'])

        await context.emit_event(process_event=PublishResumeStep.OutputEvents.ResumePublished)
