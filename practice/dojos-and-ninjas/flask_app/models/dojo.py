from flask_app.config.mysqlconnections import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self,data):
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "select * from dojos"

        results = connectToMySQL("dojos_ninjas").query_db(query)

        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def add_dojo(cls,data):
        query = "insert into dojos (name,created_at,updated_at) values(%(name)s,now(),now())"
        return connectToMySQL("dojos_ninjas").query_db(query,data)

    
    @classmethod
    def get_one(cls,data):
        query = "select * from dojos where id = %(id)s"

        result = connectToMySQL("dojos_ninjas").query_db(query,data)

        return cls(result[0])

    @classmethod
    def find_one(cls,data):
        query = "select * from dojos left join ninjas on dojos.id = ninjas.dojos_id where dojos.id=%(id)s"

        results = connectToMySQL("dojos_ninjas").query_db(query,data)

        one_dojo = cls(results[0])
        if "ninjas.id" in results[0]:
            for ninja in results:
                ninja_data = {
                    "id": ninja["ninjas.id"],
                    "first_name": ninja["first_name"],
                    "last_name": ninja["last_name"],
                    "age": ninja["age"],
                    "created_at": ninja["created_at"],
                    "updated_at": ninja["updated_at"],
                    "dojos_id": ninja["dojos_id"]
                }
            one_dojo.ninjas.append(Ninja(ninja_data))
        return one_dojo