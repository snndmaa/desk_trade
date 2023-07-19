import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def connect(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        if self.conn:
            self.conn.commit()
            self.cursor.close()
            self.conn.close()
            self.conn = None
            self.cursor = None

    def execute(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def execute_and_commit(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()

    def create_table(self, table_name, columns):
        columns_str = ', '.join(columns)
        sql = f"CREATE TABLE {table_name} ({columns_str})"
        self.execute_and_commit(sql)

    def get_columns(self, table_name):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [column[1] for column in cursor.fetchall()]

        conn.close()

        return columns

    def insert_data(self, table_name, data):
        placeholders = ', '.join(['?'] * len(data))
        sql = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(sql, data)
        self.conn.commit()

    def select_data(self, columns, table_name):
        columns_str = ', '.join(columns)
        sql = f"SELECT {columns_str} FROM {table_name}"
        return self.execute(sql)
    
    def select_condition(self, columns, table_name, col_var, var_item):
        columns_str = ', '.join(columns)
        sql = f"SELECT {columns_str} FROM {table_name} WHERE {col_var} = ?"
        return self.cursor.execute(sql, (var_item,))

    def delete_data(self, table_name, condition):
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        self.execute_and_commit(sql)
 
    def table_exist(self, table_name):
        try:
           self.select_data('*', table_name)
           return True
        except Exception as e:
            check = str(e) == f'no such table: {table_name}'
            if check:
                if table_name == 'User':
                    self.create_table("User", [
                        "ID INT AUTO_INCREMENT PRIMARY KEY",
                        "FNAME VARCHAR(30) NOT NULL",
                        "LNAME VARCHAR(30) NOT NULL",
                        "EMAIL VARCHAR(30) NOT NULL",
                        "PASSWORD VARCHAR(30) NOT NULL"
                    ])
                elif table_name == 'Asset':
                    self.create_table('Asset', [
                        'RANK INT PRIMARY KEY',
                        'NAME VARCHAR(30) NOT NULL',
                        'SYMBOL VARCHAR(4) NOT NULL',
                        'DESCRIPTION VARCHAR(200) NOT NULL',
                        'PRICE INT NOT NULL',
                        'TOTAL_SUPPLY INT',
                    ])
                elif table_name == 'Account':
                    self.create_table(
                        "ID INT AUTO_INCREMENT PRIMARY KEY",
                        "ASSETID"
                    )
            else:
                raise e
