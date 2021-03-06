from flask_restplus import fields
from src.server.instance import server

book = server.api.model('Book', {
    'id': fields.String(description='O id do registro.'),
    'title': fields.String(required=True, min_length=1, max_length=150, description='O titulo do livro')
})