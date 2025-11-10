#Poulate db with Kenyan camp sites

from app import create_app
from extensions import db
from models.activity import Activity

# 10 well-known Kenyan parks/reserves suitable as activity names
KENYAN_CAMPSITES = [
    {"name": "Maasai Mara National Reserve", "difficulty": 2},
    {"name": "Amboseli National Park", "difficulty": 1},
    {"name": "Tsavo East National Park", "difficulty": 3},
    {"name": "Tsavo West National Park", "difficulty": 3},
    {"name": "Samburu National Reserve", "difficulty": 2},
    {"name": "Lake Nakuru National Park", "difficulty": 1},
    {"name": "Hell's Gate National Park", "difficulty": 2},
    {"name": "Aberdare National Park", "difficulty": 3},
    {"name": "Mount Kenya National Park", "difficulty": 4},
    {"name": "Ol Pejeta Conservancy", "difficulty": 2},
]


def main():
    app = create_app()
    with app.app_context():
        # Optional: clear existing activities to avoid duplicates
        # WARNING: This will cascade-delete related signups per model config
        Activity.query.delete()
        db.session.commit()

        # Insert seed records
        for item in KENYAN_CAMPSITES:
            a = Activity(name=item["name"], difficulty=item["difficulty"])
            db.session.add(a)
        db.session.commit()

        count = Activity.query.count()
        print(f"Seed complete. Activities in DB: {count}")


if __name__ == "__main__":
    main()
