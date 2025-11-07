# Flask Campers Service

This project is a Flask backend service designed to manage campers, their activities, and signups for a camping program. It provides a RESTful API that allows users to perform CRUD operations on campers and activities, as well as manage signups that link campers to specific activities at designated times. The project follows the Model-View-Controller (MVC) pattern, ensuring a clean separation of concerns, and utilizes SQLAlchemy for database interactions.

## Project Structure

- **src/**: Contains the main application code.
  - **app.py**: The entry point of the application, where the Flask app is created and configured.
  - **wsgi.py**: The WSGI entry point for deploying the application.
  - **config.py**: Configuration settings for the application, including database settings.
  - **extensions.py**: Initialization of extensions like SQLAlchemy and Migrate.
  - **models/**: Contains the data models for the application.
    - **camper.py**: Defines the Camper model and its validations.
    - **activity.py**: Defines the Activity model and its validations.
    - **signup.py**: Defines the Signup model and its validations.
  - **controllers/**: Contains the logic for handling requests and responses.
    - **campers_controller.py**: Manages camper-related API endpoints.
    - **activities_controller.py**: Manages activity-related API endpoints.
    - **signups_controller.py**: Manages signup-related API endpoints.
  - **routes/**: Defines the API routes for the application.
    - **campers.py**: Contains routes related to campers.
    - **activities.py**: Contains routes related to activities.
    - **signups.py**: Contains routes related to signups.
  - **schemas/**: Defines the data schemas for validation and serialization.
    - **camper.py**: Schema for the Camper model.
    - **activity.py**: Schema for the Activity model.
    - **signup.py**: Schema for the Signup model.
  - **utils/**: Contains utility functions and validators.
    - **validators.py**: Functions for validating input data.
- **tests/**: Contains unit tests for the application.
  - **test_campers.py**: Tests for camper-related functionality.
  - **test_activities.py**: Tests for activity-related functionality.
  - **test_signups.py**: Tests for signup-related functionality.
- **migrations/**: Contains migration scripts for database schema changes.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **requirements.txt**: Lists the dependencies required for the project.
- **.env.example**: Example environment variables for configuration.
- **README.md**: Documentation for the project.

## Getting Started

1. **Clone the repository**: 
   ```
   git clone <repository-url>
   cd flask-campers-service
   ```

2. **Set up a virtual environment**:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```
   python src/app.py
   ```

## API Endpoints

- **Campers**:
  - `GET /campers`: Retrieve all campers.
  - `POST /campers`: Create a new camper.
  - `GET /campers/<id>`: Retrieve a specific camper.
  - `PUT /campers/<id>`: Update a specific camper.
  - `DELETE /campers/<id>`: Delete a specific camper.

- **Activities**:
  - `GET /activities`: Retrieve all activities.
  - `POST /activities`: Create a new activity.
  - `GET /activities/<id>`: Retrieve a specific activity.
  - `PUT /activities/<id>`: Update a specific activity.
  - `DELETE /activities/<id>`: Delete a specific activity.

- **Signups**:
  - `GET /signups`: Retrieve all signups.
  - `POST /signups`: Create a new signup.
  - `GET /signups/<id>`: Retrieve a specific signup.
  - `PUT /signups/<id>`: Update a specific signup.
  - `DELETE /signups/<id>`: Delete a specific signup.

## License

This project is licensed under the MIT License. See the LICENSE file for details.