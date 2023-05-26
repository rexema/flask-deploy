
from marshmallow_jsonapi.flask import Schema
from marshmallow_jsonapi import SchemaOpts, fields


class TagSchema(Schema):

    self_view = 'tag_detail'
    self_view_kwargs = {'id': "<id>"}
    self_view_many = 'tag_list'

    id = fields.Int(as_string=True)
    name = fields.String(allow_none=False, required=True)

    class Meta:
        type_ = 'tags'
