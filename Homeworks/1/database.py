import mysql.connector

'''
    State Maper:
        0: in-progress
        1: denied
        2: validated
'''

# # Data start:
# HOST = "mysql-2a3e420a-hastii-2c07.aivencloud.com"
# PORT = 17752
# USER = "avnadmin"
# PASSWORD = "AVNS_FLhMskMwQEoaul2OOjz"
# DATABASE = "defaultdb"


# create_table_query = '''CREATE TABLE Advertisement (
#     Id INT AUTO_INCREMENT PRIMARY KEY,
#     Description VARCHAR(250),
#     Email VARCHAR(30) NOT NULL,
#     State INT NOT NULL,
#     Category VARCHAR(128),
#     UPDATE_DATE timestamp DEFAULT CURRENT_TIMESTAMP ON UPDATE current_timestamp
#     )'''
# # End

''' 
    This class is used to connect to the database and execute queries.
'''
class Database():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host = "mysql-2a3e420a-hastii-2c07.aivencloud.com",
            port = 17752,
            user = "avnadmin",
            password = "AVNS_FLhMskMwQEoaul2OOjz",
            database = "defaultdb"
        )
        print(self.mydb)
    

    def creat_table(self, query):
        '''Create a table in the database.'''
        mycursor = self.mydb.cursor()
        mycursor.execute(query)
        self.mydb.commit()
    
    def insert_data(self, email, description, extention):
        '''Insert data into the database.'''
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO Advertisement (Description, Email, Extention, State) VALUES (%s, %s, %s, 0)"
        val = (description, email, extention)
        mycursor.execute(sql, val)

        self.mydb.commit()

        print(mycursor.rowcount, "record inserted.")
        return mycursor.lastrowid
    
    def update_data(self, id, state, category=''):
        '''Update data in the database.'''
        mycursor = self.mydb.cursor()
        sql = f"UPDATE Advertisement SET State = {state}, Category = '{category}' WHERE Id = {id}"
        mycursor.execute(sql)

        self.mydb.commit()

        print(mycursor.rowcount, "record(s) affected")

    def select_tables(self):
        '''Select all tables in the database.'''
        mycursor = self.mydb.cursor()
        mycursor.execute("SHOW TABLES")

        for x in mycursor:
            print(x)
    
    def select_by_id(self, id):
        '''Select a row by id.'''
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT * FROM Advertisement WHERE ID={id}")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)

        return myresult

    def alter_table(self):
        '''Alter table to add extention column.'''
        mycursor = self.mydb.cursor()
        mycursor.execute(f"ALTER TABLE Advertisement ADD extention varchar(10)")
        self.mydb.commit()
    

    def delete_row(self, id):
        '''Delete a row by id.'''
        mycursor = self.mydb.cursor()
        mycursor.execute(f"DELETE FROM Advertisement WHERE Id = {id}")
        self.mydb.commit()


    def get_email(self, id):
        '''Get email by id.'''
        mycursor = self.mydb.cursor()
        mycursor.execute(f"SELECT Email FROM Advertisement WHERE Id = {id}")

        myresult = mycursor.fetchall()
        return myresult[0][0]
        


# db = Database(HOST, PORT, USER, PASSWORD, DATABASE)
# # db.select_tables()
# # db.creat_table(create_table_query)
# Database().insert_data('hastii@gmail.com', 'test')
# for id in range(1, 6):
#     Database().delete_row(id)

# Database().select_by_id(27)
