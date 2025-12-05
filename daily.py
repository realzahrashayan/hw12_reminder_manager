from dataclasses import dataclass
import logging
from base import BaseReminder



@dataclass
class DailyRoutineReminder(BaseReminder):
    daily_repeat:bool = False

    def remind(self):
        logger = logging.getLogger("reminderlogger")
        if self.daily_repeat:
            text = "daily repeat is active"
        else:
            text = "daily repeat in not active"
        message = f"{self.title}-situation:{text}"

        logger.info(f"dailyreminder : {message}")
        print(message)

    