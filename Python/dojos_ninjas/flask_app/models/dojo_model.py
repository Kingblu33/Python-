from winreg import QueryInfoKey
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def savedojo(cls,data):
        query = "Insert INTO burgers (name,bun,meat,calories,created_at,updated_at) VALUES(%(name)s,%(bun)s,%(meat)s,%(calories)s,NOW(),NOW());"
        results = connectToMySQL('dojos_ninjas').query_db(query,data)
        return results
    @classmethod
    def selectalldojos(cls)
        query="SELECT * FROM dojos WHERE"

