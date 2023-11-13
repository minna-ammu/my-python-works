import mysql.connector            # module

db=mysql.connector.connect(       # function
    host="localhost",
    user="root",                  # python database um ayi connection establish chaeythu. from db to print(db) vare
    password="_Mysql@1996_"
)
print(db)

cursor=db.cursor()                # cursror object ne call cheythu. python il ninn database lottum thirichym data kai maran cursor object ne create cheythu.
query="create database animal"
cursor.execute(query)
