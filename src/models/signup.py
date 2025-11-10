from datetime import datetime
from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import db

class Signup(db.Model):
    __tablename__ = 'signups'

    id = Column(Integer, primary_key=True)
    camper_id = Column(Integer, ForeignKey('campers.id'), nullable=False)
    activity_id = Column(Integer, ForeignKey('activities.id'), nullable=False)
    signup_time = Column(DateTime, default=datetime.utcnow)

    camper = relationship('Camper', back_populates='signups')
    activity = relationship('Activity', back_populates='signups')

    def __repr__(self):
        return f'<Signup {self.id} - Camper {self.camper_id} for Activity {self.activity_id}>'