from base import BaseReminder
import logging



class ReminderManger():
    def __init__(self):
        self._reminders:list = []
        self.logger = logging.getLogger("ReminderLogger")


    def add_reminder(self,reminder):
        self._reminders.append(reminder)
        self.logger.info(f"reminder with ID : {reminder.reminder_id} is added")


    def remove(self,reminder_id):
        for each in self._reminders:
            if each.reminder_id == reminder_id:
                self._reminders.remove(each)
                self.logger.warning(f"reminder with ID : {reminder_id} is removed") 
                return True
        self.logger.error(f"removing reminder with ID : {reminder_id} is not successful")    
        return False


    def list_reminder(self):
        if not self._reminders:
            print("we cant find any Reminders!")
            return
        
        for each in self._reminders:
            print(f"[{each.reminder_id}] - {each.title} - {each.time}")

    def find_by_id(self,remind_id:int):
        for item in self._reminders:
            if item.reminder_id == remind_id:
                return item
        return None
    

    def execute_all(self):
        if not self._reminders:
            print(f"we dont hane any reminder please try again!")
            self.logger.warning(f"execte is called but there is no reminder! ")
            return
        
        for data in self._reminders:
            self.logger.info("reminder with id_number : {data.reminder_id} is active!")
            try:
                data.remind()
            except Exception as e :
                self.logger.error("reminder with id_number : {data.reminder_id} has error :{e}")

    def group_reminder(self):
        """groping them with their names"""
        if not self._reminders:
            print("There is no reminder here!")
            return
        
        group={}

        for x in self._reminders:
            group_name = x.__class__.__name__
            if group_name not in group:
                group[group_name]=[] #age vojod nadashte bashe misaze
            
            group[group_name].append(x)

        for key,value in group.items():
            print(f"\n---{key}--")
            for reminder in value:
                print(f"ID={reminder.reminder_id} | {reminder.title}  | {reminder.time}")



    def reminder_types(self):#shows uniq reminder type
        types = {r.__class__.__name__ for r in self._reminders}
        print("Reminder types used:")
        for t in types:
            print(f"- {t}")
        return types
