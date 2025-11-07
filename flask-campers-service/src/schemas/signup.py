from marshmallow import Schema, fields

class SignupSchema(Schema):
    id = fields.Int(dump_only=True)
    camper_id = fields.Int(required=True)
    activity_id = fields.Int(required=True)
    signup_time = fields.DateTime(required=True)