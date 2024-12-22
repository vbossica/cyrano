import os
from knack.config import CLIConfig

CLI_ENV_VARIABLE_PREFIX = 'cyrano_'


def _get_config_dir() -> str:
    config_dir = os.getenv('CYRANO_CONFIG_DIR', None) or \
        os.path.expanduser(os.path.join('~', '.cyrano'))
    if not os.path.exists(config_dir):
        os.makedirs(config_dir)
    return config_dir


GLOBAL_CONFIG_DIR = _get_config_dir()
GLOBAL_CONFIG = CLIConfig(config_dir=GLOBAL_CONFIG_DIR)
