#utf-8

from pymongo import MongoClient

connection = MongoClient("localhost",27017)
mydb = connection.mydb # new a database
myser = mydb.hengsengindex # new a table

listdic = []

def getindex():
    dbs = myser.find()
    for item in dbs:
        listdic.append(item)
    return listdic    
