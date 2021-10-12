from flask import Flask
from flask_restplus import Api, Resource
from src.server.instance import server

app, api = server.app, server.api

books_db = [
    {'id': 0, 'title': 'War of Peace'},
    {'id': 1, 'title': 'clean code'}
]

@api.route('/books')
class booklist(Resource):
    def get(self, ):
        return books_db

    def post(self, ):
        response = api.payload
        books_db.append(response)
        return response, 200