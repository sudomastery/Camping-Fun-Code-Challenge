from extensions import db
from sqlalchemy.orm import validates

class Camper(db.Model):
    __tablename__ = "campers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    # One camper has many signups
    signups = db.relationship("Signup", back_populates="camper")

    @validates("name")
    def validate_name(self, _, value):
        # Concept: validations raise ValueError; routes will format {"errors": ["validation errors"]}
        if not value or not str(value).strip():
            raise ValueError("validation errors")
        return str(value).strip()

    @validates("age")
    def validate_age(self, _, value):
        # Must be an integer 8..18 (inclusive)
        if not isinstance(value, int) or value < 8 or value > 100:
            raise ValueError("@fucked validation errors")
        return value

    # Small helper used by API responses (list and create endpoints)
    def to_dict_basic(self):
        return {"id": self.id, "name": self.name, "age": self.age}
