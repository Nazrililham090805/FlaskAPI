import psycopg2
from models.book import Book  

# Function to establish a database connection
def db_conn():
    url = "postgresql://postgres:Nazril0908@localhost:5432/postgres"
    return psycopg2.connect(url)

# Function to retrieve all books from the database
def get_all_books():
    try:
        # Connect to database
        connection = db_conn()
        cursor = connection.cursor()
        
        # Query all books from the Book_View
        cursor.execute('''SELECT * FROM public."Book"''')
        data = cursor.fetchall()

        # Create Book objects from the retrieved data
        books = [Book(
            Book_ID=book[0],
            Title=book[1],
            Description=book[2],
            ISBN=book[3],
            language_id=book[4],
            edition_id=book[5],
            year_id=book[6],
            
        ) for book in data]
        # print('test')
        return books, None
    except Exception as e:
        return [], str(e)
    finally:
        # Close connection to database
        if connection:
            cursor.close()
            connection.close()

# Function to retrieve books by a specific author
def get_books_by_language(language):
    try:
        connection = db_conn()
        cursor = connection.cursor()

        # Query books of a specific author
        cursor.execute('''SELECT * FROM public."Book" WHERE "languange_id" IN ( SELECT "language_id "  FROM public."Language" WHERE "language_name" = %s)''', (language,))
        data = cursor.fetchall()

        # Create Book objects from the retrieved data
        books = [Book(
            Book_ID=book[0],
            Title=book[1],
            Description=book[2],
            ISBN=book[3],
            language_id=book[4],
            edition_id=book[5],
            year_id=book[6],
        ) for book in data]
        print(books)
        if books:
            return books, None
        else:
            raise ValueError('Book is not found')
    except Exception as e:
        return [], str(e)
    finally:
        # Close connection to database
        if connection:
            cursor.close()
            connection.close()

