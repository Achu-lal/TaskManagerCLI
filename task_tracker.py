import json
import os
from task import Task

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

    def add_task(self,description):
        task_id = len(self.task) + 1
        new_task = Task(task_id,description)
        self.task.append(new_task.to_dict())
        self.save_tasks()


if __name__ == '__main__':
    manager = TaskManager()
    manager.add_task("Finish the task tracker project 2")
