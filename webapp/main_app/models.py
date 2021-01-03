from sqlalchemy.orm import relationship
from datetime import datetime

from webapp.model import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    Done = db.Column(db.Boolean)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
    
    user_id = db.Column(
        db.Integer,
        db.ForeignKey('user.id', ondelete='CASCADE'),
        index=True
    )
    
    user = relationship('User', backref='todo')
    
    def __repr__(self):
        return '<Id {}>'.format(self.id)