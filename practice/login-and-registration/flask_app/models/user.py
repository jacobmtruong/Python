from flask import flash
from flask_app.config.mysqlconnections import connectToMySQL
import re

NAME_REGEX = re.compile (r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self,data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @staticmethod
    def validate_user(user):
        is_valid = True

        if not NAME_REGEX.match(user['first_name']) and len(user['first_name']) < 2:
            flash ("First name has letters only and at least 2 characters")
            is_valid = False

        if not NAME_REGEX.match(user['last_name']) and len(user['last_name']) < 2:
            flash ("Last name has letters only and at least 2 characters")
            is_valid = False

        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False

        if len(user['password']) < 8:
            flash("Password needs to have at least 8 charecters")
            is_valid = False

        if user['password'] != user['confirm_password']:
            flash("Passwords must match")
            is_valid = False

        return is_valid

    @classmethod
    def register(cls,data):
        query = "insert into users (first_name, last_name, email, password, created_at, updated_at) values(%(first_name)s, %(last_name)s, %(email)s, %(password)s, now(), now());"

        return connectToMySQL("login_registration").query_db(query,data)

    @classmethod
    def get_user_by_email(cls,data):
        query = 'select * from users where email = %(email)s;'

        results = connectToMySQL("login_registration").query_db(query,data)
        #did't find a matching user
        if len(results) < 1:
            return False
        return cls(results[0])


    @classmethod
    def get_user_by_id(cls,data):
        query = 'select * from users where id = %(id)s;'

        results = connectToMySQL("login_registration").query_db(query,data)

        return cls(results[0])