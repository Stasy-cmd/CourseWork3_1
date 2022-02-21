from marshmallow import fields, Schema


class FavoriteMovieSchema(Schema):
    user_id = fields.Int()
    user = fields.Str()
    movie_id = fields.Int()
    movie = fields.Str()
