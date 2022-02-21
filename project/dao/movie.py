from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_one(self, mid):
        return self._db_session.query(Movie).get(mid)

    def get_all(self):
        return self._db_session.query(Movie).all()

    def get_by_director_id(self, did):
        return self._db_session.query(Movie).filter(Movie.director_id == did).all()

    def get_by_genre_id(self, did):
        return self._db_session.query(Movie).filter(Movie.genre_id == did).all()

    def get_by_year(self, did):
        return self._db_session.query(Movie).filter(Movie.year == did).all()

    def create(self, movie_d):
        new_movie = Movie(**movie_d)
        self._db_session.add(new_movie)
        self._db_session.commit()
        return  new_movie

    def delete(self, rid):
        movie = self.get_one(rid)
        self._db_session.delete(movie)
        self._db_session.commit()

    def update(self, movie_d):
        movie = self.get_one(movie_d.get("id"))
        movie.title = movie.get("title")
        movie.description = movie.get("description")
        movie.trailer = movie.get("trailer")
        movie.year = movie.get("year")
        movie.rating = movie.get("rating")
        movie.genre_id = movie.get("genre_id")
        movie.director_id = movie.get("director_id")

        self._db_session.add(movie)
        self._db_session.commit()
