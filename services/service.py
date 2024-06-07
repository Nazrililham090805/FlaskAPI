from repository.RepoBook import get_all_books, get_books_by_language
from repository.RepStore import delete_store_by_Store_name, add_Store


def get_all_books_service():
    return get_all_books()

def get_books_by_language_service(language):
    return get_books_by_language(language)

def delete_store_by_Store_name_service(Store_name):
    return delete_store_by_Store_name(Store_name)

def add_store_service(store_name, phone, email, address_id):
    return add_Store(store_name, phone, email, address_id)