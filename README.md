## Camping Fun API

Lightweight Flask backend for managing campers, activities, and signups (many-to-many via a join model). Built as a learning, step-by-step challenge.

### Stack
- Python 3 + Flask application factory (`create_app` in `src/app.py`)
- Flask-SQLAlchemy ORM models (`Camper`, `Activity`, `Signup`)
- Flask-Migrate (Alembic) for schema versioning
- SQLite dev database

### Core Models
- Camper: id, name (non-empty), age (8–18 inclusive), relationship: signups
- Activity: id, name (non-empty), difficulty (int), relationship: signups (cascade delete-orphan)
- Signup: id, time (0–23), camper_id FK, activity_id FK, relationships back to camper/activity

### Validation
Model-level `@validates` raise `ValueError`; routes translate any failure to a unified JSON: `{ "errors": ["validation errors"] }` per challenge spec.

### API Endpoints (Port 5555)
Base URL: `http://localhost:5555`

| Method | Path | Description | Success | Error |
|--------|------|-------------|---------|-------|
| GET | /campers | List campers | 200 `[ {id,name,age}, ... ]` | - |
| GET | /campers/<id> | Camper detail w/ signups + nested activity | 200 `{id,name,age,signups:[...]}` | 404 `{"error":"Camper not found"}` |
| POST | /campers | Create camper | 201 `{id,name,age}` | 400 `{"errors":["validation errors"]}` |
| PATCH | /campers/<id> | Update camper (name/age) | 202 `{id,name,age}` | 404 / 400 |
| GET | /activities | List activities | 200 `[ {id,name,difficulty}, ... ]` | - |
| POST | /activities | Create activity | 201 `{id,name,difficulty}` | 400 |
| DELETE | /activities/<id> | Delete activity (cascades signups) | 204 empty | 404 `{"error":"Activity not found"}` |
| POST | /signups | Create signup | 201 `{id,time,camper_id,activity_id,activity:{...},camper:{...}}` | 400 |

### Quick Start
1. Create & activate virtual env (optional).
2. Install deps:
	```
	pip install -r requirements.txt
	```
3. Initialize DB (first time):
	Set Flask app for CLI (PowerShell):
	```powershell
	$env:FLASK_APP = "src.app:create_app"
	```
	```
	flask db init   # already done in repo perhaps
	flask db migrate -m "initial"
	flask db upgrade
	```
4. Run server:
	```
	python src/app.py
	```
5. Seed activities (optional):
	```
	python src/seed.py
	```

### Sample Requests (PowerShell)
Create Camper:
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5555/campers -Body (@{name='Amina';age=12} | ConvertTo-Json) -ContentType 'application/json'
```
Create Activity:
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5555/activities -Body (@{name='Lake Naivasha Bird Walk';difficulty=1} | ConvertTo-Json) -ContentType 'application/json'
```
Create Signup:
```powershell
Invoke-RestMethod -Method Post -Uri http://localhost:5555/signups -Body (@{camper_id=1;activity_id=1;time=9} | ConvertTo-Json) -ContentType 'application/json'
```

### Error Shape
All validation problems resolve to:
```json
{"errors": ["validation errors"]}
```
Missing records use `{"error":"<Entity> not found"}`.

### Development Notes
- Cascade delete ensures removing an Activity cleans related Signups.
- Importing `models` inside `create_app()` guarantees Alembic sees tables.
- Serialization helpers keep route logic lean.

### Next Possible Enhancements
- Add automated tests (pytest) for each endpoint & validation edge cases.
- More granular error messages (currently simplified by spec).
- Pagination for list endpoints.
- Camper & signup seed script.

### Deep Dive Guide
See `OFFLINE_GUIDE.md` (if present) for exhaustive explanations of architecture, decisions, and learning notes.

---
Happy camping! 🏕️
