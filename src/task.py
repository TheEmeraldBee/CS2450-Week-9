class Task:
    def __init__(self):
        title = ""
        description = ""
        due_date = ""
        status = False

    def set_title(self, s):
        self.title = s
        
    def set_description(self,s):
        self.description = s
    
    def set_due_date(self, s):
        self.due_date = s

    def set_status(self,b):
        self.status = b

    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_due_date(self):
        return self.due_date
    
    def get_status(self):
        return self.status