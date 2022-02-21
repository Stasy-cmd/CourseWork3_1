from flask_restx import abort, Namespace, Resource

from project.exceptions import ItemNotFound
from project.services.directors_service import DirectorsService
from project.setup_db import db

director_ns = Namespace("directors")


@director_ns.route("/")
class MoviesView(Resource):
    @director_ns.response(200, "OK")
    def get(self):
        """Get all directors"""
        return DirectorsService(db.session).get_all_directors()


@director_ns.route("/<int:genre_id>")
class MovieView(Resource):
    @director_ns.response(200, "OK")
    @director_ns.response(404, "Director not found")
    def get(self, director_id: int):
        """Get Director by id"""
        try:
            return DirectorsService(db.session).get_item_by_id(director_id)
        except ItemNotFound:
            abort(404, message="Director not found")
