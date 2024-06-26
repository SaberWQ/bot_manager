from flask_login import UserMixin
from project.settings import  DATABASE

class User(DATABASE.Model, UserMixin):
    id = DATABASE.Column(DATABASE.Integer, primary_key = True)
    
    login = DATABASE.Column(DATABASE.String(40), nullable = False)
    password = DATABASE.Column(DATABASE.String(50), nullable = False)
    is_admin = DATABASE.Column(DATABASE.Boolean)

    def __repr__(self) -> str:
        return f'id: {self.id}'