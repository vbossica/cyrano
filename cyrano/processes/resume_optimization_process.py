from enum import Enum
from cyrano.steps.load_resume_step import LoadResumeStep
from cyrano.steps.optimize_resume_step import OptimizeResumeStep
from cyrano.steps.publish_resume_step import PublishResumeStep
from semantic_kernel.processes.process_builder import ProcessBuilder
from semantic_kernel.processes.process_function_target_builder import ProcessFunctionTargetBuilder


class ResumeOptimizationProcess(ProcessBuilder):
    """
    The process that optimizes the resume based on the job requirements.
    """

    class ProcessEvents(Enum):
        OptimizeResumeEvent = 'OptimizeResumeEvent'

    @staticmethod
    def create_process() -> ProcessBuilder:
        process_builder = ProcessBuilder('optimize_resume')

        # add the steps
        load_resume_step = process_builder.add_step(LoadResumeStep)
        optimize_resume_step = process_builder.add_step(OptimizeResumeStep)
        publish_resume_step = process_builder.add_step(PublishResumeStep)

        # add the events binding the steps
        process_builder.on_input_event(ResumeOptimizationProcess.ProcessEvents.OptimizeResumeEvent)\
            .send_event_to(ProcessFunctionTargetBuilder(load_resume_step))
        load_resume_step.on_event(LoadResumeStep.OutputEvents.ResumeLoaded)\
            .send_event_to(target=optimize_resume_step, parameter_name='data')
        optimize_resume_step.on_event(OptimizeResumeStep.OutputEvents.ResumeOptimized)\
            .send_event_to(ProcessFunctionTargetBuilder(publish_resume_step))

        return process_builder
