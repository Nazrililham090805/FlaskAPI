from flask import Flask
from Routes.BookRoute import book_blueprint
from Routes.StoreRoute import store_blueprint


app = Flask(__name__)
app.register_blueprint(book_blueprint)
app.register_blueprint(store_blueprint)