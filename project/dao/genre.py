from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, pk):
        return self._db_session.query(Genre).filter(Genre.id == pk).one_or_none()

    def get_all(self):
        return self._db_session.query(Genre).all()

    def create(self, genre_d):
        ent = Genre(**genre_d)
        self._db_session.add(ent)
        self._db_session.commit()
        return ent

    def delete(self, gid):
        genre = self.get_by_id(gid)
        self._db_session.delete(genre)

    def update(self, genre_d):
        genre = self.get_by_id(genre_d.get("id"))
        genre.name = genre_d.get("name")

        self._db_session.add(genre)
        self._db_session.commit()
