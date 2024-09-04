import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Zaneera333",
    database="student"

)
print(db)
cursor = db.cursor()
selectquery="select* from student"
cursor.execute(selectquery)
records=cursor.fetchall()
print("--")
# import MySQLdb

# db = MySQLdb.connect(
#     host="localhost",
#     user="root",
#     passwd="Zaneera333",
#     db="student"
# )
# cursor = db.cursor()

