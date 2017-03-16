#coding:utf-8

from pymongo import MongoClient
import json

connection = MongoClient("localhost",27017)
mydb = connection.mydb # new a database
myser = mydb.allindex # new a table

# namelist = ['上证50','上证指数','上证180','沪深300','恒生指数','恒生指数H','上证380','红利指数','中证红利','中证500','深证100R']


def getindex(indexname):
    
    namelist = ['上证50','恒生指数H','红利指数','上证180','沪深300']
    listdic = []

    print indexname
    if indexname:
       print namelist
       namelist = [indexname]
       print 'ceshi'
       print namelist

    datas = []

    for item in namelist:
        dicn = {}
        dicn['indexname'] = item
        dbs = myser.find(dicn)
    # dbs = myser.find({'indexname':'沪深300'})
        pes = []
        for item in dbs:
            listdic.append(item)
            dic = {}
            datestring = item['date']
            datestring = datestring.encode('utf-8')
            dic['date'] = datestring
            dic['earyeild'] = item['earyeild']
            indexstring = item['index']
            if indexstring:
               index = float(indexstring)
               dic['index'] = index

            pes.append(dic) 
        pes = json.dumps(pes)
        datas.append(pes)

    print type(datas)
    datas = json.dumps(datas)
    return datas

