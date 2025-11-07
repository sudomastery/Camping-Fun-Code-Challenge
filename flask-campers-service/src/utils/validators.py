def validate_camp_id(camp_id):
    if not isinstance(camp_id, int) or camp_id <= 0:
        raise ValueError("Camp ID must be a positive integer.")

def validate_activity_id(activity_id):
    if not isinstance(activity_id, int) or activity_id <= 0:
        raise ValueError("Activity ID must be a positive integer.")

def validate_signup_data(data):
    if not isinstance(data, dict):
        raise ValueError("Signup data must be a dictionary.")
    if 'camper_id' not in data or 'activity_id' not in data:
        raise ValueError("Signup data must include 'camper_id' and 'activity_id'.")
    validate_camp_id(data['camper_id'])
    validate_activity_id(data['activity_id'])