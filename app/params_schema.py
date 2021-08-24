from marshmallow import Schema, fields, ValidationError

class CreateSessionSchema(Schema):
    room_id = fields.Int(required=True)
    start_timestamp = fields.Str(required=True)

class UpdateSessionSchema(Schema):
    room_id = fields.Int(required=True)
    start_timestamp = fields.Str(required=True)
    seq_num = fields.Int(required=True)