from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def createdojo(cls,data):
        query = "INSERT into dojos (name,location,language,comment) VALUES (%(name)s,%(location)s,%(language)s,%(comment)s);"
        results = connectToMySQL('dojo_survey').query_db(query,data)
        return results

    @classmethod
    def retrievedojo(cls):
        query = "SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;"
        results = connectToMySQL('dojo_survey').query_db(query)
        return (results[0])
    @staticmethod
    def validate_dojo(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name needs to be 3 characters.")
        if len(dojo['location']) < 1:
            is_valid = False
            flash("Must choose a dojo location.")
        if len(dojo['language']) < 1:
            is_valid = False
            flash("Didnt choose a favorite language.")
        if len(dojo['comment']) < 3:
            is_valid = False
            flash("Comments must be at least 3 characters.")

        return is_valid

