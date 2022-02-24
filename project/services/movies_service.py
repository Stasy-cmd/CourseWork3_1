from project.dao.movie import MovieDAO
from project.exceptions import ItemNotFound
from project.schemas.movie import MovieSchema
from project.services.base import BaseService


class MoviesService(BaseService):
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        movies = MovieDAO(self._db_session).get_by_id(pk)
        if not movies:
            raise ItemNotFound
        return MovieSchema().dump(movies)

    def get_all_movies(self, filters):
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all(rid)
        return movies

    def create(self, pk):
        return self.dao.create(pk)

    def update(self, pk):
        self.dao.update(pk)
        return self.dao

    def delete(self, pk):
        self.dao.delete(pk)
