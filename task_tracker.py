import json
import os

class TaskManager:
    def __init__(self,file_name = 'task.json'):
        self.file_name = file_name
        self.task = self.load_task()

    def load_task(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name,'w') as file:
                json.dump([],file)
            return []
        
        with open(self.file_name,'r') as file:
            return json.load(file)
        
    def save_tasks(self):
        with open(self.file_name,'w') as file:
            json.dump(self.task,file,indent=4) 
task_manager = TaskManager()
task_manager.load_task()