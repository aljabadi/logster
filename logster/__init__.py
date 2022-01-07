# This script can be used in any codebase to enable formatted logging
# all you need to do is import 'setup_logger'
# function from this script and follow the docs for creating a logger object.
# Alternatively, you can simply import the 'LOGGER' object for a development env
import logging


class LogColourFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    magneta = "\x1b[35m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: magneta + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


def setup_logger(name=None, level="INFO"):
    """set up python formatted logger for console logging

    Args:
        name (str, optional): Name of the logger. Defaults to None.
        Must follow dot notation if using parent/child loggers. See logging
        docs for detaiils.
        level (string): One of ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        Passed to:
        https://docs.python.org/3/library/logging.html#logging.Logger.setLevel.
        Defaults to 'INFO'.

    Returns:
        A logging object with formats and console handler
    """
    # https://docs.python.org/3/howto/logging-cookbook.html#multiple-handlers-and-formatters
    logger = logging.getLogger(name)
    # global debug level - specifies what to track
    logger.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    # handler debug level
    level = logging.__dict__[level]
    ch.setLevel(level)
    ch.setFormatter(LogColourFormatter())
    logger.addHandler(ch)
    return logger
