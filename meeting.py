from dataclasses import dataclass,field
import logging
from base import BaseReminder



@dataclass
class MeetingReminder(BaseReminder):
    participants:list[str] = field(default_factory=list)

    def remind(self):
        logger = logging.getLogger("RemindLogger")
        if self.participants:
            last_participant = ",".join(self.participants)
        else:
            last_participant = "we don't have partipants"
        message = f"meetingreminder : {self.title} -> persons : {last_participant}"
        logger.info("meetingreminder : {message}")
        print(message)
