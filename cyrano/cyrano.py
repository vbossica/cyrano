from knack import CLI
from cyrano.common.config import CLI_ENV_VARIABLE_PREFIX, GLOBAL_CONFIG_DIR
from cyrano.common.logmodule import init_logging
from .cyrano_commands import CyranoCommandsLoader
from .cyrano_help import CyranoHelp

CLI_NAME = 'cyrano'


class Cyrano(CLI):
    """
    Main class for the CLI.
    """

    def __init__(self) -> None:
        super(Cyrano, self).__init__(
            cli_name=CLI_NAME,
            config_dir=GLOBAL_CONFIG_DIR,
            config_env_var_prefix=CLI_ENV_VARIABLE_PREFIX,
            commands_loader_cls=CyranoCommandsLoader,
            help_cls=CyranoHelp)
        init_logging('cyrano.log')
        self.args = None
