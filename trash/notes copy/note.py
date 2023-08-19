from datetime import date, datetime

class Note:
    
    def __init__(self, id="", title="", body="", date=date.today):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def info(self):
        result = f"{self.id};{self.title};{self.body};{self.date}"
        return result
    
    def __str__(self):
        result = f"{self.id};{self.title};{self.body};{self.date}"
        return result
    
    def to_json(self):
        return {'id': self.id, 'title': self.title, 'body': self.body, 'date': date.strftime(self.date, '%Y-%m-%d')}