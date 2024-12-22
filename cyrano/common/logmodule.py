import logging


def init_logging(filepath, level=logging.DEBUG) -> None:
    """
    Initialize the logging module for the application.

    :param filepath: path to the logfile
    """
    logger = logging.getLogger()
    logger.setLevel(level)

    # create a file handler for all levels
    file_handler = logging.FileHandler(filepath)
    file_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    # create a console handler for the error messages
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
    logger.addHandler(console_handler)
