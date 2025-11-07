from marshmallow import Schema, fields

class ActivitySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str()
    duration = fields.Int(required=True)  # Duration in minutes
    max_participants = fields.Int(required=True)  # Maximum number of participants
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)