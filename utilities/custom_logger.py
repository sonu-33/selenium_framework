import logging
import os


def get_logger(logger_name: str = "ZSeleniumFramework"):
    logs_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "logs")
    os.makedirs(logs_dir, exist_ok=True) # computes a logs directory path; creates it if it does not exist

    log_file = os.path.join(logs_dir, "test.log")
    logger = logging.getLogger(logger_name) # creates a logger named ZSeleniumFramework
    if not logger.handlers: # avoids adding duplicate handlers if logger already exists
        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s" # sets the format of the logs
        )

        file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler) # writes logs to test.log

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler) # prints logs to console

        logger.propagate = False # disables propagation so the logger does not duplicate messages

    return logger
