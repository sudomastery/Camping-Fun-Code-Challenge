from extensions import db
from sqlalchemy.orm import validates

class Activity(db.Model):
    __tablename__ = "activities"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String, nullable=False)
    
    difficulty = db.Column(db.Integer, nullable=False)

    
    signups = db.relationship(
        "Signup",
        back_populates="activity",
        cascade="all, delete-orphan"
    )

    @validates("name")
    def validate_name(self, _, value):
        if not value or not str(value).strip():
            raise ValueError("validation errors")
        return str(value).strip()

    @validates("difficulty")
    def validate_difficulty(self, _, value):
        if not isinstance(value, int):
            raise ValueError("validation errors")
        return value

    def to_dict_basic(self):
        return {"id": self.id, "name": self.name, "difficulty": self.difficulty}