import psycopg2

class ClientManager:
    def __init__(self, db_name, user, password):
        self.conn = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS clients (
            id SERIAL PRIMARY KEY,
            first_name VARCHAR(60),
            last_name VARCHAR(60),
            email VARCHAR(60),
            phone VARCHAR(60)
        );
        """
        self.cursor.execute(query)
        self.conn.commit()

    def add_client(self, first_name, last_name, email):
        query = """INSERT INTO clients (first_name, last_name, email) VALUES (%s, %s, %s);"""
        self.cursor.execute(query, (first_name, last_name, email))
        self.conn.commit()
        print("Client added successfully")

    def add_phone(self, client_id, phone):
        query = "UPDATE clients SET phone = %s WHERE id = %s"
        self.cursor.execute(query, (phone, client_id))
        self.conn.commit()
        print("Phone added successfully")

    def update_client(self, client_id, first_name=None, last_name=None, email=None):
        query = "UPDATE clients SET first_name = %s, last_name = %s, email = %s WHERE id = %s"
        self.cursor.execute(query, (first_name, last_name, email, client_id))
        self.conn.commit()
        print("Client updated successfully")

    def delete_phone(self, client_id):
        query = "UPDATE clients SET phone = NULL WHERE id = %s"
        self.cursor.execute(query, (client_id,))
        self.conn.commit()
        print("Phone deleted successfully")

    def delete_client(self, client_id):
        query = "DELETE FROM clients WHERE id = %s"
        self.cursor.execute(query, (client_id,))
        self.conn.commit()
        print("Client deleted successfully")

    def find_clients(self, search_term):
        query = "SELECT * FROM clients WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s OR phone LIKE %s"
        search_term = f"%{search_term}%"
        self.cursor.execute(query, (search_term, search_term, search_term, search_term))
        results = self.cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No clients found")

    def display_all_clients(self):
        query = "SELECT * FROM clients"
        self.cursor.execute(query)
        results = self.cursor.fetchall()
        if results:
            for row in results:
                print(row)
        else:
            print("No clients found")