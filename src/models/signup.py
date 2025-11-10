# FILE: flask-campers-service/src/models/signup.py
from extensions import db
from sqlalchemy.orm import validates

class Signup(db.Model):
    __tablename__ = "signups"

    id = db.Column(db.Integer, primary_key=True)

    # Hour of the day (0..23)
    time = db.Column(db.Integer, nullable=False)

    camper_id = db.Column(
        db.Integer,
        db.ForeignKey("campers.id"),
        nullable=False
    )
    activity_id = db.Column(
        db.Integer,
        db.ForeignKey("activities.id"),
        nullable=False
    )

    # Relationships back to parents
    #many to many
    camper = db.relationship("Camper", back_populates="signups")
    activity = db.relationship("Activity", back_populates="signups")

    @validates("time")
    def validate_time(self, _, value):
        # Must be an integer 0..23 inclusive
        if not isinstance(value, int) or value < 0 or value > 23:
            raise ValueError("validation errors")
        return value

    # Serializer that nests activity (used in GET /campers/<id>)
    def to_dict_with_activity(self):
        return {
            "id": self.id,
            "time": self.time,
            "camper_id": self.camper_id,
            "activity_id": self.activity_id,
            "activity": self.activity.to_dict_basic() if self.activity else None,
        }

    # Serializer that nests both sides (used in POST /signups success example)
    def to_dict_full(self):
        return {
            "id": self.id,
            "time": self.time,
            "camper_id": self.camper_id,
            "activity_id": self.activity_id,
            "activity": self.activity.to_dict_basic() if self.activity else None,
            "camper": self.camper.to_dict_basic() if self.camper else None,
        }