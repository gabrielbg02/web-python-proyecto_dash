from pymongo import MongoClient


client = MongoClient ('localhost',27017)

database = client.red
chat = database.chat 

chat.insert_one({"nombre" : "maria", "apellido" : "hanoun", "edad": 88 })

for nombre in chat.find():
    print (nombre)



