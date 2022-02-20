from flask import Flask,request, jsonify
from omdb import Omdb
import sqlite3
import os

currentdir = os.path.dirname(__file__)

app = Flask(__name__)
omdb = Omdb()

@app.route('/')
def index():
    return 'Task-Python Developer'

@app.route('/search/<searchtype>/<search_keyword>')
def search(searchtype, search_keyword):
    searchtype = searchtype.lower()
    data = get_movie(searchtype,search_keyword)
    if len(data):
        return jsonify(data)
    else:
        if searchtype in omdb.get_param_keys():
            response_data = omdb.get(searchtype, search_keyword).json()
            add_movie(response_data)
            return jsonify(response_data)

def add_movie(data):
    id = data['imdbID']
    title = data['Title']
    year = data['Year']
    rating = data['imdbRating']
    genrus = data['Genre']
    connection = sqlite3.connect(currentdir + '/movie_data.db')
    cursor = connection.cursor()
    query = "INSERT INTO movies VALUES('{id}', '{title}', '{year}', '{rating}','{genrus}')" .format(id=id, title=title, year=year, rating=rating, genrus=genrus)
    result = cursor.execute(query)
    connection.commit()

def get_columns():
    return ['id', 'title', 'year', 'rating', 'genrus']

def get_movie(searchtype, search_keyword):
    response = []
    if searchtype in get_columns():
        connection = sqlite3.connect(currentdir + '/movie_data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM movies WHERE {type} LIKE '%{value}%'" .format(type=searchtype, value=search_keyword)
        result = cursor.execute(query)
        response = result.fetchall()
        
    return response
