from enum import Enum
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from semantic_kernel.processes.kernel_process.kernel_process_step import KernelProcessStep
from semantic_kernel.processes.kernel_process.kernel_process_step_context import KernelProcessStepContext


class LoadResumeStep(KernelProcessStep):

    class OutputEvents(Enum):
        ResumeLoaded = 'ResumeLoaded'

    @kernel_function
    async def run(self,
                  context: KernelProcessStepContext,
                  data: dict) -> None:
        """
        Load the resume from the file and set it in the context.
        """

        experiences = self._load_file(data['experiences_file'])
        requirements = self._load_file(data['requirements_file'])

        await context.emit_event(process_event=LoadResumeStep.OutputEvents.ResumeLoaded,
                                 data={
                                     'experiences': experiences,
                                     'requirements': requirements
                                 })

    def _load_file(self, file_path: str) -> str:
        print(f'Load file {file_path}')
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
