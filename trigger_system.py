"""
Problem name: trigger system

Core idea:
"Something happens → others react automatically"

Key benefit:
"I can add/remove reactions without touching main logic"

Signal to use:
"When one action should cause many independent actions"
"""


from abc import ABC, abstractmethod


class Database:
    def __save_to_db(self, data):
        # save data on db
        if data:
            self.db.append(data)
            return 0
        return 1

    def __check_file(self, file):
        return 0 if file else 1

    def save_file(self, file):
        if not self.__check_file:
            result = self.__save_to_db(file)
            if result:
                return 0
            return "there was a problem with saving file on database"
        else:
            return "the file was not in right format"

class Email:
    def notify(self, notification):
        print(f"{notification} has been sent")
    
    def handle(self, data):
        print(f"Email sent for {data}")

class SMSNotification:
    def notify(self, notification):
        print(f"{notification} has been sent")
    
    def handle(self, data):
        print(f"SMS sent for {data}")

class ILog(ABC):
    @abstractmethod
    def logging(self, log): pass

class Logger(ILog):  
    def logging(self, log):
        print(f"{log} action has been executed")
    
    def handle(self, data):
        print(f"Logged {data}")


class Analytics:
    def update_analytics(self, data):
        print(f"analytics has been updated with {data}")
    
    def handle(self, data):
        print(f"Analytics updated with {data}")

class File:
    def __init__(self, trigger_system):
        self.trigger_system = trigger_system

    def __upload_file(self, file):
        self.database.save_file(file)

    def __trigger(self, msg):
        self.trigger_system.trigger(msg)

    def upload_file_and_trigger(self, file):
        self.__upload_file(file)
        self.__trigger(file)

class TriggerSystem:
    def __init__(self):
        self.listeners = []
    
    def register(self, listener):
        self.listeners.append(listener)

    def trigger(self, data):
        for listener in self.listeners:
            listener.handle(data)
    
trigger = TriggerSystem()
trigger.register(Email())
trigger.register(Logger())
trigger.register(Analytics())
trigger.register(SMSNotification())
file = File()
file.upload_file_and_trigger("file", trigger)