from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user_model


class Painting: 
    db = "artist_paintings_schema"

    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.price = data['price']
        self.created_at = data['updated_at']
        self.updated_at = data['created_at']
        self.artist_id = data['artist_id']


        self.artistting = {}

    @staticmethod
    def validate_paintings(form_data):
        is_valid = True
        if len(form_data['title']) < 3 :
            flash ("Title has to be atleast 3 characters")
            is_valid = False
        if len(form_data['description']) < 3 :
            flash ("Title has to be atleast 3 characters")
            is_valid = False
        print(form_data['price'],'*************************')
        if form_data['price'] == '':
            flash("price cant be a string")
            is_valid=False
            return is_valid

        if int(form_data['price']) < 10:
            flash ("price has to be atleast $10")
            is_valid = False

        return is_valid

    @classmethod
    def add_painting(cls,data):
        query= "INSERT INTO paintings (title,description,price,artist_id) VALUES( %(title)s,%(description)s,%(price)s,%(artist_id)s)"
        results=connectToMySQL(cls.db).query_db(query,data)

        return results

    @classmethod
    def get_one_painting(cls,data):
        query="SELECT * FROM paintings WHERE id=%(id)s"
        results=connectToMySQL(cls.db).query_db(query,data)
        return cls(results[0])

    @classmethod
    def udpate_painting(cls,data):
        query = "UPDATE paintings SET title=%(title)s,description=%(description)s,price=%(price)s,artist_id=%(artist_id)s WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data) 

    
    @classmethod
    def showone(cls,data):
        query= "SELECT * FROM paintings LEFT JOIN artists on artists.id=paintings.artist_id WHERE paintings.id=%(id)s"
        results=results=results = connectToMySQL(cls.db).query_db(query,data)
        
        artist=cls(results[0])

        artist_data={
            "id" : results[0]["artists.id"],
            "first_name" : results[0]["first_name"],
            "last_name" : results[0]["last_name"],
            "email" : results[0]["email"],
            "password" : results[0]["password"],
            "created_at" : results[0]["artists.created_at"],
            "updated_at" : results[0]["artists.updated_at"]
        }

        artist_instance=user_model.User(artist_data)

        artist.artistting=artist_instance

        return artist


    @classmethod
    def delete_paint(cls,data):
        query="DELETE FROM paintings WHERE id=%(id)s "
        return connectToMySQL(cls.db).query_db(query,data)