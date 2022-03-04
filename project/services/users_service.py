from project.dao.user import UserDAO
from project.exceptions import ItemNotFound
from project.schemas.user import UserSchema
from project.services.base import BaseService
from project.dao.models.user import User

class UsersService(BaseService):
    def __init__(self, session):
        self.session = session

    def get_user_by_id(self, uid):
        user = self.session.query(User).get_by_id(uid)
        if not user:
            raise ItemNotFound
        return UserSchema().dump(user)

    def get_all_users(self):
        users = self.session.query(User).get_all()
        return UserSchema(many=True).dump(users)

    def create(self, uid):
        user = self.session.query(User).create(uid)
        return UserSchema().dump(user)

    def update(self, uid):
        self.session.query(User).update(uid)

    def delete(self, uid):
        self.session.query(User).delete(uid)

    def get_item_by_email(self, email):
        user = self.session.query(User).filter(User.email == email).one()
        return UserSchema ().dump ( user )
        