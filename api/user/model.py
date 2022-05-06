#!/usr/bin/env python3
from datetime import datetime

from api.core.db_manager import db, get_db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    phone = db.Column(db.String(30), nullable=True, index=True)
    email = db.Column(db.String(120), unique=True)

    created_at = db.Column(db.DateTime, unique=False, nullable=False, index=True, default=datetime.utcnow())

    deleted = db.Column(db.Boolean(), nullable=False, default=False)

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f'<User {self.name}>'

    def save(self) -> None:
        db_instance = get_db()
        db_instance.session.add(self)
        db_instance.session.commit()

    def delete(self) -> None:
        db_instance = get_db()
        self.deleted = True
        db_instance.session.add(self)
        db_instance.session.commit()

    @classmethod
    def deserialize(cls,
                    data: dict,
                    save: bool = False) -> 'User':
        """
        Deserialize a dictionary with format:
        {
          "email": "some@email.com",
          "name": "Igor",
          "phone": "+390622334455"
        }
        And create an session with it

        If you want to save the instance in the database then send the save option to True

        :param data: serialize dict with the data for the User
        :type data: dict
        :param save: says if need to perform the save into the database
        :type save: bool
        :return: The User
        """
        user = User(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone")
        )

        if save:
            user.save()

        return user