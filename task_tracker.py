import json
import os
from task import Task
import argparse

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
        try:
            task_id = len(self.task) + 1  
            new_task = Task(task_id, description)
            self.task.append(new_task.to_dict()) 
            self.save_tasks()   
            print(f"Task '{description}' added with ID: {task_id}")
        except Exception as e:
            print(f"Error adding task: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Task Manager CLI")
    parser.add_argument('command',choices=['add'],help='Command to execute')
    parser.add_argument('--description',type=str, help='description of the task')

    args = parser.parse_args()

    task_manager = TaskManager()

    if args.command == 'add':
        if args.description:
             task_manager.add_task(args.description)
        else:
            print("Error: Please provide a task description using --description.")
