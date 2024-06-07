from flask import Blueprint, jsonify, request
from services.service import get_all_books_service, get_books_by_language_service

book_blueprint = Blueprint('books', __name__)

@book_blueprint.route('/api/book', methods=['GET'])
def get_books():
    books, error_msg = get_all_books_service()

    if books:
        books_list = [{
            'book_id': book.Book_id,
            'Title': book.Title,
            'Description': book.Description,
            'ISBN': book.ISBN,
            'language_id': book.language_id,
            'edition_id': book.edition_id,
            'year_id': book.year_id,
        } for book in books]

        print(books)
        return jsonify({'books': books_list}), 200
    else: 
        return jsonify({'message': 'Failed to pick up book', 'error': error_msg}), 404
    
    


@book_blueprint.route('/api/book/<language>', methods=['GET'])
def get_books_by_language(language):
    books, error_msg = get_books_by_language_service(language)
    print(books)

    if books:
        books_list = [{
            'book_id': book.Book_id,
            'Title': book.Title,
            'Description': book.Description,
            'ISBN': book.ISBN,
            'language_id': book.language_id,
            'edition_id': book.edition_id,
            'year_id': book.year_id,
        } for book in books]

        return jsonify({'books': books_list}), 200
    else: 
        return jsonify({'message': 'Failed to pick up book', 'error': error_msg}), 404
    
    
