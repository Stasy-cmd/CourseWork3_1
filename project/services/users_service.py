from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.base import BaseService

class UsersService(BaseService):
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_user_by_id(self, uid):
        user = UserDAO(self._db_session).get_by_id(uid)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = UserDAO(self._db_session).get_all()
        return UserSchema(many=True).dump(users)

    def create(self, uid):
        return self.dao.create(uid)

    def update(self, uid):
        self.dao.update(uid)

    def delete(self, uid):
        self.dao.delete(uid)

    def get_item_by_email(self, email):
        pass