from sqlalchemy import Column, Integer, String, Text
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Activity(db.Model):
    __tablename__ = 'activities'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    duration = Column(Integer, nullable=False)  # Duration in minutes

    def __repr__(self):
        return f'<Activity {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'duration': self.duration
        }