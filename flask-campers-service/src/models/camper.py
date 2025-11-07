from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Camper(db.Model):
    __tablename__ = 'campers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    activities = db.relationship('Signup', backref='camper', lazy=True)

    def __repr__(self):
        return f'<Camper {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email
        }