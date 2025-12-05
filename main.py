from simple import SimpleReminder
from daily import DailyRoutineReminder
from meeting import MeetingReminder
from logger import set_logger
from manager import ReminderManger
import logging



def main():
    set_logger()
    logger = logging.getLogger("ReminderLogger")
    logger.info("the program is started")
    manager1 = ReminderManger() 

    r1 = SimpleReminder(title= "buy bread",time="10:30")
    r2 = DailyRoutineReminder(title="practice python",time="8:30",daily_repeat=True)
    r3 = MeetingReminder(title="meeting with backend developer",time="13:30",participants=["zahra","camu","ali"])
    r4 = MeetingReminder(title="meeting with no one",time="16:30")

   
    manager1.add_reminder(r1)
    manager1.add_reminder(r2)
    manager1.add_reminder(r3)
    manager1.add_reminder(r4)
    # manager1.list_reminder()
    print(manager1.find_by_id(1))
    # manager1.group_reminder()


if __name__=="__main__":
    main()