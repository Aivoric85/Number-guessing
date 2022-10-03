import sqlite3



#Getting User Name from Database
connect = sqlite3.connect("Data/User/User.db")
connect.text_factory = str
cursor = connect.cursor()
cursor.execute("SELECT * FROM User")
data = cursor.fetchall()
#print(data)
name = data[0][1]
lang = data[0][2]
#print(name, lang)
connect.close()

