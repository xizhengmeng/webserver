# -*- coding: utf-8 -*-
import urllib2,time,urllib
import ast,os,sys,string
from pymongo import MongoClient

months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dicts = {'zsgz00':'no','zsgz10':'上证指数','zsgz20':'上证180','zsgz30':'上证50','zsgz40':'沪深300','zsgz50':'深证成指','zsgz60':'深证100R','zsgz70':'中小板指','zsgz80':'上证380','zsgz90':'红利指数','zsgz100':'中证红利','zsgz110':'中证500'}

connection = MongoClient("localhost",27017)
mydb = connection.mydb # new a database
myser = mydb.hengsengindex # new a table

def getindexs():

    downLoadStr = 'http://www.csindex.com.cn/sseportal/ps/zhs/hqjt/csi/show_zsgz.js'
    print downLoadStr
    try:
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
                 "Referer": 'http://www.baidu.com'}
        req = urllib2.Request(downLoadStr, headers=i_headers)  
        f = urllib2.urlopen(req)
        data = f.read()
        str = data.decode('gbk')
        data = str.encode('utf-8')
        print data
        listString = data.split('\n')

        date = ''
        index = 0
        for item in listString:
            if 'zsgz00' in item:
               date = item[12:-2]
               datelist = list(date)
               for s in datelist:
                   if s == '-':
                      datelist.remove(s)
               date = ''.join(datelist)
               print date
            if '0=' in item:
               pe = listString[index + 1]
               pb = listString[index + 3]
               rate = listString[index + 4]
               indexitem = item.index('=')
               indexpe = pe.index('=')
               indexpb = pb.index('=')
               indexrate = rate.index('=')
               pe = pe[indexpe+2:-2]
               pb = pb[indexpe+2:-2]
               rate = rate[indexpe+2:-2]
               item = item[indexitem+2:-2]
               print item
               
               pe = filter(lambda ch: ch in '.0123456789', pe)
               pb = filter(lambda ch: ch in '.0123456789', pb)
               rate = filter(lambda ch: ch in '.0123456789', rate)

               if len(pe) and len(pb) and len(rate):
                  roaf = float(pe)
                  roe = 1/roaf * 100
                  dbs = myser.find({'指数名称':item,'日期':date})
                  count = 0
                  for item in dbs:
                      count = count + 1
                  if count == 0:
                    myser.save({'指数名称':item,'市盈率':pe,'盈利收益率':roe,'日期':date,'市净率':pb,'股息率':rate})

            index = index + 1

    except Exception,ex:
        print ex
    

def gethenghseng(day,month,year):
    
    yearStr = '%i' % year
    yearList = list(yearStr)
    yearStr1 = yearList[-1]
    yearStr2 = yearList[-2]
    yearStr = yearStr2 + yearStr1
    
    monthStr = months[month - 1]
    
    targetStr = 'idx_%i%s%s' % (day,monthStr,yearStr)
    
    fileName = '/root/apps/data/localdata/%i%s%s.txt' % (day,monthStr,yearStr)
    
    downLoadStr = 'http://sc.hangseng.com/gb/www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/report/hsi/' + targetStr + '.csv'
    print downLoadStr
    try:
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
            "Referer": 'http://www.baidu.com'}
        req = urllib2.Request(downLoadStr, headers=i_headers)
        f = urllib2.urlopen(req)
        data = f.read()
        f = open(fileName,'wb')
        f.write(data)
        f.close()
        
        f1 = open(fileName,'rb')
        dataList = f1.readlines()
        item  = dataList[2]
        list2 = item.split('	')
        date = list2[0]
        index = list2[5]
        roa = list2[9]
        date = filter(lambda ch: ch in '0123456789', date)
        index = filter(lambda ch: ch in '.0123456789', index)
        string = filter(lambda ch: ch in '.0123456789', roa)
        roaf = float(string)
        roe = 1/roaf * 100
        print date
        print index
        dbs = myser.find({'指数名称':'恒生指数','日期':date})
        count = 0
        for item in dbs:
            count = count + 1
        if count == 0:
          myser.save({'指数名称':'恒生指数','市盈率':roaf,'盈利收益率':roe,'日期':date,'指数':index}) # add a record
        
          saveStr = '%s  %f' % (date, roe)
          
          f = open('hengseng.txt','r')
          data = f.read()
          f.close()
          
          dataStr = data + '\n' + saveStr
          f = open('hengseng.txt','w')
          f.write(dataStr)
          f.close()
    except Exception,ex:
        print ex


def gethenghsengchina(day,month,year):
    
    yearStr = '%i' % year
    yearList = list(yearStr)
    yearStr1 = yearList[-1]
    yearStr2 = yearList[-2]
    yearStr = yearStr2 + yearStr1
    
    monthStr = months[month - 1]
    
    targetStr = 'idx_%i%s%s' % (day,monthStr,yearStr)
    
    fileName = '/root/apps/data/localdata/china%i%s%s.txt' % (day,monthStr,yearStr)
    
    downLoadStr = 'http://sc.hangseng.com/gb/www.hsi.com.hk/HSI-Net/static/revamp/contents/en/indexes/report/hscei/' + targetStr + '.csv'
    print downLoadStr
    try:
        i_headers = {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5",\
            "Referer": 'http://www.baidu.com'}
        req = urllib2.Request(downLoadStr, headers=i_headers)
        f = urllib2.urlopen(req)
        data = f.read()
        f = open(fileName,'wb')
        f.write(data)
        f.close()
        
        f1 = open(fileName,'rb')
        dataList = f1.readlines()
        item  = dataList[2]
        list2 = item.split('	')
        date = list2[0]
        index = list2[5]
        roa = list2[9]
        date = filter(lambda ch: ch in '0123456789', date)
        index = filter(lambda ch: ch in '.0123456789', index)
        string = filter(lambda ch: ch in '.0123456789', roa)
        roaf = float(string)
        roe = 1/roaf * 100
        
        print index
        dbs = myser.find({'指数名称':'恒生指H','日期':date})
        count = 0
        for item in dbs:
            count = count + 1
        if count == 0:
          myser.save({'指数名称':'恒生指数H', '市盈率':roaf,'盈利收益率':roe,'日期':date,'指数':index})
          
          saveStr = '%s  %f' % (date, roe)
          
          f = open('hengsengchina.txt','r')
          data = f.read()
          f.close()
          
          dataStr = data + '\n' + saveStr
          f = open('hengsengchina.txt','w')
          f.write(dataStr)
          f.close()
    except Exception,ex:
        print ex


current = time.localtime(time.time())
year = current.tm_year
month = current.tm_mon
day = current.tm_mday

index = 0
if month == 12:
   index = 1

index = month - 1

day = day - 1

# gethenghseng(day,month,year)

#for month in xrange(1,3):
#   for day in xrange(1,31):
gethenghsengchina(day,month,year)
gethenghseng(day,month,year)
getindexs()

