from dataclasses import dataclass,field
import logging
from base import BaseReminder



@dataclass
class SimpleReminder(BaseReminder):

    def remind(self):
        logger = logging.getLogger("ReminderLogger")
        message = f"it's time to : {self.title}"
        logger.info(f"simplereminder : {message}")
        print(message)
        
