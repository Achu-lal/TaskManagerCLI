from datetime import datetime

class Task:
    def __init__(self,task_id,description):
            self.id = task_id
            self.description = description
            self.status = 'todo'
            self.created_at = datetime.now().isoformat()
            self.updated_at = datetime.now().isoformat()

    def update_status(self,new_status):
          self.status = new_status
          self.updated_at = datetime.now().isoformat

    def to_dict(self):
          
          return {
                'id' : self.id,
                'description' : self.description,
                'status' : self.status,
                'createdAt' : self.created_at,
                'updatedAt' : self.updated_at
          }