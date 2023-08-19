from datetime import date, datetime

class Note:
    
    def __init__(self, id="", title="", body="", date=date.today):
        self.id = id
        self.title = title
        self.body = body
        self.date = date
    
    def __str__(self):
        result = f"id: {self.id}, title: {self.title}, body: {self.body}, date: {date.strftime(self.date, '%Y-%m-%d')}"
        return result
    
    def to_dict(self):
        result = dict()
        result["id"] = self.id
        result["title"] = self.title
        result["body"] = self.body
        result["date"] = date.strftime(self.date, '%Y-%m-%d')
        return result
    
    def from_dict(self, inDict: dict):
        self.id = inDict["id"]
        self.title = inDict["title"]
        self.body = inDict["body"]
        self.date = datetime.strptime(inDict["date"], '%Y-%m-%d').date()
        return self