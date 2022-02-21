from project.dao.models.base import BaseMixin
from project.setup_db import db


class User(BaseMixin, db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True, required=True)
    email = db.Column(db.String(255), unique=True, required=True)
    password = db.Column(db.String(255), required=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    favorite_genre = db.Column(db.String(255), nullable=False)
