from project.dao.favorite_movie import FavoriteMovieDAO
from project.exceptions import ItemNotFound
from project.schemas.favorite_movie import FavoriteMovieSchema
from project.services.base import BaseService



class FavoriteMovieService(BaseService):
    def __init__(self, dao: FavoriteMovieDAO):
        self.dao = dao

    def get_item_by_id(self, pk):
        fav_movie = FavoriteMovieDAO(self._db_session).get_by_id(pk)
        if not fav_movie:
            raise ItemNotFound
        return FavoriteMovieSchema().dump(fav_movie)