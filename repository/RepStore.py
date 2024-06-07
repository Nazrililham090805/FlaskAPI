import psycopg2
from models.store import store 

# Function to establish a database connection
def db_conn():
    url = "postgresql://postgres:Nazril0908@localhost:5432/postgres"
    return psycopg2.connect(url)

def delete_store_by_Store_name(Store_name):
    try: 
        connection = db_conn()
        cursor = connection.cursor()

        # Begin transaction
        cursor.execute('''BEGIN TRANSACTION''')

        # Query to get Store ID from Store name
        cursor.execute('''SELECT "Store_ID" FROM public."Store" WHERE "Store_Name" = %s''', (Store_name,))
        Store_ID = cursor.fetchone()

        # Check if the Store exists
        if Store_ID:
            Store_ID = Store_ID[0]

            # Delete related entries from other tables
            cursor.execute('''DELETE FROM public."Staff" WHERE "Store_id" = %s''', ((Store_ID,)))
            cursor.execute('''DELETE FROM public."Store_Book" WHERE "Store_Store_ID" = %s''', ((Store_ID,)))
            cursor.execute('''DELETE FROM public."Store" WHERE "Store_ID" = %s''', ((Store_ID,)))
      
        else:
            raise ValueError('Book not found')
        
        # Commit the transaction
        connection.commit()
        return True, None
    except Exception as e:
        if connection:
            connection.rollback() # Rollback the transaction if an exception occurs
        return False, str(e)
    finally:
        # Close connection to database
        if connection:
            cursor.close()
            connection.close()


def add_Store(Store_name, email, phone, address_id):
    try:
        connection = db_conn()
        cursor = connection.cursor()

        # Begin transaction
        cursor.execute('''BEGIN TRANSACTION''')

        cursor.execute('''SELECT "address_id" FROM public."Address" WHERE "address_id" = %s''', (address_id,))
        address_id = cursor.fetchone()

        cursor.execute('''SELECT MAX("Store_ID") FROM public."Store"''')
        Store_id = cursor.fetchone()[0] + 1  # Increment the maximum ReviewsID

        if address_id:
            address_id = address_id[0]
        else:
            raise ValueError("There is no such store")
        
        cursor.execute('''INSERT INTO public."Store"("Store_ID", "Store_Name", "Phone", "Email", address_id)VALUES (%s, %s, %s, %s, %s)''', (Store_id, Store_name, phone, email, address_id))

        connection.commit()
        return True, None
    except Exception as e:
        if connection:
            connection.rollback() # Rollback the transaction if an exception occurs
            return False, str(e)
    finally:
    # Close connection to database
        if connection:
            cursor.close()
            connection.close()



            
