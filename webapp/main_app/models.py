from webapp.model import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200))
    Done = db.Column(db.Boolean)
    
    def __repr__(self):
        return '<Id {}>'.format(self.id)