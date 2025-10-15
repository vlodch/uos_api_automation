import logging
import os
from config import LOG_LEVEL


def get_logger(name: str):

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    log_dir = os.path.join(os.getcwd(), "logs")
    os.makedirs(log_dir, exist_ok=True)

    file_handler = logging.FileHandler(os.path.join(log_dir, "test.log"))

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(name)s: %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    logger.setLevel(LOG_LEVEL)
    return logger
