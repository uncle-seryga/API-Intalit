import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("database.db",check_same_thread=False)
        self.cursor = self.connection.cursor()
        # todo: Add DB structure " CREATE TABLE IF NOT EXISTS - USERS, PRODUCTS
    def get(self):
        pass
    def update(self):
        pass
    def post(self):
        pass
    def delete(self):
        pass

class Users(Database):
    table_name = 'users'
    def get(self):
        pass

class Products(Database):
    table_name = 'product'
