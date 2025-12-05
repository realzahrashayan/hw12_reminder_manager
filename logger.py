import logging

def set_logger():
    logging.basicConfig(
        filename="reminder.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        encoding="utf-8"

    )