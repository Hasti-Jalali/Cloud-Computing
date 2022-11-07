import mysql.connector

# Data start:
HOST = "mysql-2a3e420a-hastii-2c07.aivencloud.com"
PORT = 17752
USER = "avnadmin"
PASSWORD = "AVNS_FLhMskMwQEoaul2OOjz"
DATABASE = "Test"

create_table_query = "CREATE TABLE users (name VARCHAR(255) primary key, address VARCHAR(255))"

# End
class Database():

    def __init__(self, HOST, PORT, USER, PASSWORD, DATABASE):
        mydb = mysql.connector.connect(
            host = HOST,
            port = PORT,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )
        print(mydb)
    
    def creat_table(self, query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)

    def insert_data(self, dict_values):
        mycursor = self.mydb.cursor()
        table_name = 'something'
        sql = f"INSERT INTO {table_name} (name, address) VALUES (%s, %s)"
        val = ("John", "Highway 21")
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")
