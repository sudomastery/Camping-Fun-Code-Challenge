from marshmallow import Schema, fields, validate

class CamperSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    age = fields.Int(required=True, validate=validate.Range(min=0))
    email = fields.Str(required=True, validate=validate.Email())
    activities = fields.List(fields.Str(), dump_only=True)  # List of activity IDs or names associated with the camper