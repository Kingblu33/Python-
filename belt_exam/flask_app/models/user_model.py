from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import painting_model
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 



class User: 
    db = "artist_paintings_schema"

    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['updated_at']
        self.updated_at = data['created_at']

        self.paintings = {}


    @staticmethod
    def validate_info(form_data):
        is_valid=True
        if len(form_data["first_name"]) < 3 :
            flash("First Name needs to be more than three(3) characters")
            is_valid=False

        if len(form_data["last_name"]) < 3 :
            flash("last Name needs to be more than three(3) characters")
            is_valid=False
        if len(form_data["password"]) < 3 :
            flash("Password needs to be more than three(3) characters")
            is_valid=False
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        if len(form_data["password"]) < 5:
            flash("password needs to be longer than 5 characters")
            is_valid=False

        if form_data["password"] != form_data["confirm_password"]:
            flash("passwords dont match")
            is_valid=False

        return is_valid
    @classmethod
    def save_new_user(cls,data):
        query="INSERT INTO artists (first_name,last_name,email,password,updated_at,created_at) VALUES ( %(first_name)s,%(last_name)s,%(email)s,%(password)s,NOW(),NOW());"
        results = connectToMySQL(cls.db).query_db(query,data)
        return results
    
    @classmethod
    def login(cls,data):
        query="SELECT * FROM artists WHERE email=%(email)s;"
        results=connectToMySQL(cls.db).query_db(query,data)

        if len(results) < 1:
            return False

        return cls(results[0])

    @classmethod
    def getall(cls):
        query="SELECT * FROM artists JOIN paintings ON artists.id=paintings.artist_id "
        results = connectToMySQL(cls.db).query_db(query)
        
        
        all_artist=[]

        for data in results :
            artist=cls(data)
            paintings_data= {
                "id":data['paintings.id'],
                "title":data['title'],
                "description":data['description'],
                "price":data["price"],
                "artist_id":data['artist_id'],
                "created_at" : data["paintings.created_at"],
                "updated_at" : data["paintings.updated_at"],
        }
            
            artist.paintings= painting_model.Painting(paintings_data)

            all_artist.append(artist)


        return all_artist


    @classmethod 
    def getoneartist(cls,data):
        query="SELECT * FROM artists WHERE id=%(id)s"
        results = connectToMySQL(cls.db).query_db(query,data)

        return  cls(results[0])

    