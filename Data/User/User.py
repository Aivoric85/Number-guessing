import sqlite3

def create_user():
    connect = sqlite3.connect("Data/User/User.db")
    connect.text_factory = str
    cursor = connect.cursor()
    cursor.execute("SELECT *, MAX(id) FROM User")
    data = cursor.fetchall()
    #print(data)
    id = data[0][0]
    #name = data[0][1]
    #lang = data[0][2]
    #score = data [0][3]
    print(id)
    id = id +1
    name = 'Alf'
    lang = 'de'
    score = 10
    data = ([id, name, lang, score])
    cursor.execute("INSERT INTO User VALUES(?,?,?,?)", data)
    connect.commit()
    connect.close()

   




#Getting User Name from Database
#connect = sqlite3.connect("Data/User/User.db")
#connect.text_factory = str
#cursor = connect.cursor()
#cursor.execute("SELECT *, MAX(id) FROM User")
#data = cursor.fetchall()
#print(data)
#id = data[0][0]
#name = data[0][1]
#lang = data[0][2]
#score = data [0][3]
#print(id, name, lang, score)
#connect.close()

create_user()

