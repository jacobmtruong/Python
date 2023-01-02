from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash


class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojos_id = data ["dojos_id"]

    @staticmethod
    def validate_ninja(ninja):
        is_valid = True
        



    @classmethod
    def get_all(cls):
        query = "select * from ninjas"

        results = connectToMySQL("dojos_ninjas").query_db(query)

        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def save(cls,data):
        query = "insert into dojos_ninjas.ninjas (first_name,last_name,age,created_at,updated_at,dojos_id) values(%(first_name)s,%(last_name)s,%(age)s,now(),now(),%(dojos_id)s)"
        return connectToMySQL("dojos_ninjas").query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = "delete from ninjas where id = %(id)s;"

        result = connectToMySQL("dojos_ninjas").query_db(query,data)

        return result