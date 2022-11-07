import mysql.connector

# Data start:
HOST = "mysql-2a3e420a-hastii-2c07.aivencloud.com"
PORT = 17752
USER = "avnadmin"
PASSWORD = "AVNS_FLhMskMwQEoaul2OOjz"
DATABASE = "defaultdb"


create_table_query = '''CREATE TABLE Advertisement (
    Id INT AUTO_INCREMENT PRIMARY KEY,
    Description VARCHAR(250),
    Email VARCHAR(30) NOT NULL,
    State INT NOT NULL,
    Category VARCHAR(128),
    UPDATE_DATE timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE current_timestamp
    )'''
# End

''' 
    This class is used to connect to the database and execute queries.
'''
class Database():

    def __init__(self, HOST, PORT, USER, PASSWORD, DATABASE):
        self.mydb = mysql.connector.connect(
            host = HOST,
            port = PORT,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )
        print(self.mydb)
    

    def creat_table(self, query):
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        self.mydb.commit()
    
    def insert_data(self, email, description):
        mycursor = self.mydb.cursor()
        table_name = 'Advertisement'
        sql = f"INSERT INTO {table_name} (Description, Email, State) VALUES (%s, %s, %d)"
        val = (email, description, 0)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        return mycursor.lastrowid
    
    def update_data(self, id, state, category=''):
        mycursor = self.mydb.cursor()
        table_name = 'Advertisement'
        sql = f"UPDATE {table_name} SET (State, Category) VALUES (%d, %s) WHERE Id = %d"
        val = (state, category, id)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

    def select_tables(self):
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)
    
    def select_rows(self, table_name):
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM {table_name}")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)


db = Database(HOST, PORT, USER, PASSWORD, DATABASE)
# db.select_tables()
# db.creat_table(create_table_query)
db.select_rows('Advertisement')
