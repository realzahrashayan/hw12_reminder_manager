from generator import get_next_id
from dataclasses import dataclass,field
import logging


@dataclass
class BaseReminder():
    title:str
    time:str
    reminder_id:int = field(default_factory=get_next_id ,init=False)

    def __post_init__(self):
        logger = logging.getLogger("ReminderLogger")


        if not self.title:
            logger.error("title is empty")
            raise ValueError("title can't be empty")
        
        if not self.time:
            logger.error("time is empty")
            raise ValueError("time can't be empty")
        
        logger.info(f"the new reminder is created - id = {self.reminder_id} , title = {self.title}")
        
    def remind(self): 
        raise NotImplementedError("subclasses must implement remind()")
    

    
        
