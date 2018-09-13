import pymysql

conn = pymysql.connect(
    host= "localhost",
    port= 3306
    user= "root",
    passwd= "",
    db= "mysql",
    charset= "utf-8"
    )

cursor = conn.cursor()

sql_query = "SELECT * FROM USER"
cursor.execute(sql_query)

results = cursor.fetchall()
#for row in results:
#    name = row[0]
#    lname = [0]

# jika menggunakan insert, update, delete
# conn.commit()


cursor.close()
conn.close()
