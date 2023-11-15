import sqlite3

class Database:
    _instance = {}

    def __new__(cls, db_name):
        if db_name not in cls._instance:
            cls._instance[db_name] = super(Database, cls).__new__(cls)
            cls._instance[db_name].db_name = db_name
            cls._instance[db_name].conn = None
            cls._instance[db_name].connect()
            return cls._instance[db_name]
        
        raise Exception("Use database exported from 'modules/Database.py'")
        

    def connect(self):
        if not self.conn:
            self.conn = sqlite3.connect(self.db_name)

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def create_table(self, table_name, columns):
        self.connect()
        cursor = self.conn.cursor()
        columns_str = ', '.join(f'{key} {value}' for key, value in columns.items())
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})")
        self.conn.commit()

    def insert_data(self, table_name, data):
        self.connect()
        cursor = self.conn.cursor()
        placeholders = ', '.join(':' + key for key in data.keys())
        cursor.execute(f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({placeholders})", data)
        self.conn.commit()

    def update_data(self, table_name, data, condition):
        self.connect()
        cursor = self.conn.cursor()
        set_values = ', '.join([f'{key} = :{key}' for key in data.keys()])
        cursor.execute(f"UPDATE {table_name} SET {set_values} WHERE {condition}", data)
        self.conn.commit()

    def query_data(self, query):
        self.connect()
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def __del__(self):
        self.close()


database = Database('database/telematics.db')