from sqlalchemy.orm.scoping import scoped_session

from project.dao.models.user import User


class UserDAO:
    def __init__(self, session: scoped_session):
        self._db_session = session

    def get_by_id(self, uid):
        return self._db_session.query(User).filter(User.id == uid).one_or_none()

    def get_all(self):
        return self._db_session.query(User).all()

    def create(self, user_d):
        user = User(**user_d)
        self._db_session.add(user)
        self._db_session.commit()
        return user

    def delete(self, uid):
        user = self.get_by_id(uid)
        self._db_session.delete(user)

    def update(self, user_d):
        user = self.get_by_id(user_d.get("id"))
        user.name = user_d.get("name")
        user.email = user_d.get("email")
        user.password = user_d.get("password")
        user.surname = user_d.get("surname")
        user.favorite_genre = user_d.get("favorite_genre")

        self._db_session.add(user)
        self._db_session.commit()
