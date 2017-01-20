#coding:utf-8
import os,datetime
from django.http import HttpResponse
from django.shortcuts import render
from DIY.compute import getModelFromJson
from DIY.createui import getCreatedStringWithProperties
from django.http import HttpResponseRedirect
from DIY.mail import sendMail
from DIY.APIServer import getfilecontent,writecontent,checkfile,createfolder
import shutil
import logging
import commands,time
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

#def some_view(request):
    #...

#logger = logging.getLogger(__name__)

def home(request):
    string = '这是'
    return render(request,'home.html',{'string':string})

def nextPage(request):
    return render(request,'next.html')

def compute(request):
    string = request.GET['text']
    string = getModelFromJson(string)
    return HttpResponse(string)

def uicreate(request):
    return render(request,'UICreate.html')

def webserver(request):
    return render(request,'WebServer.html')

def webserverfullre(request):
    return render(request,'WebServerFull.html')

def createui(request):
    string = request.GET['text']
    string = getCreatedStringWithProperties(string)
    return HttpResponse(string)

def package(request):
    return render(request,'package.html')

def jsonFormat1(request):
    return HttpResponseRedirect('http://www.jsonparseronline.com')

def jsonFormat2(request):
    return HttpResponseRedirect('http://www.sojson.com')    

def interfaceTest(request):
    return HttpResponseRedirect('http://www.atool.org/httptest.php')

def blockClickview(request):
    return HttpResponseRedirect('http://www.hanson647.com')    

def upload_file(request):

    if request.method == "POST":
        myFile1 =request.FILES.get("myfile1", None)
        myFile2 =request.FILES.get("myfile2", None)

        filePathTemp = '/Users/wxg/Documents/upload/'
        filePath = '/Users/wxg/Documents/JDJRAPPAndroid/JDJR/libs/'
        filePathN = filePath + 'armeabi/'

        if myFile1:
           targetPath = filePath + myFile1.name
           targetPathN = filePathN + myFile1.name

           filePahtEnd = ''
           if os.path.exists(targetPath):
               filePahtEnd = filePath
           elif os.path.exists(targetPathN):
               filePahtEnd = filePathN
           else:
               return HttpResponse('fail-----%s is not exist' % myFile1.name)

           destination = open(os.path.join(filePahtEnd, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

           destination1 = open(os.path.join(filePathTemp, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination1.write(chunk)
           destination1.close()

        if myFile2:
           targetPath = filePath + myFile2.name
           targetPathN = filePathN + myFile2.name

           filePahtEnd = ''
           if os.path.exists(targetPath):
              filePahtEnd = filePath
           elif os.path.exists(targetPathN):
               filePahtEnd = filePathN
           else:
               return HttpResponse('fail-----%s is not exist' % myFile2.name)

           destination = open(os.path.join(filePahtEnd, myFile2.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

           destination1 = open(os.path.join(filePathTemp, myFile2.name),'wb+')
           for chunk in myFile2.chunks():
               destination1.write(chunk)
           destination1.close()

        #filelistStr = ''
        #count = 0
        #for filename in os.listdir(filePath):
            #if filename[0] != '.':
               #count = count + 1
               #filename = '(%.0f)'  % count + filename + '_____'
               #filelistStr += filename

        #return HttpResponse('upload over!' + 'dir list:' + filelistStr)
        os.chdir('/Users/wxg/Documents/JDJRAPPAndroid')
        text = os.popen('git status')
        textStr = text.read()

        return HttpResponse('success' +'<br>'+ textStr)

def upload_urls_file(request):
    if request.method == "POST":
        text = request.POST.get('inputId')
        if (text):
            print text
        else:
            return HttpResponse('失败---------请输入接口标识')

        myFile1 =request.FILES.get("myfile1", None)
        myFile2 =request.FILES.get("myfile2", None)
        myFile3 =request.FILES.get("myfile3", None)
        myFile4 =request.FILES.get("myfile4", None)
        myFile5 =request.FILES.get("myfile5", None)
        myFile6 =request.FILES.get("myfile6", None)
        myFile7 =request.FILES.get("myfile7", None)

        filePath = '/Users/wxg/Documents/APIServer/' + text

        if (not os.path.exists(filePath)):
            os.mkdir(filePath)

        if myFile1:
           destination = open(os.path.join(filePath, myFile1.name),'wb+')
           for chunk in myFile1.chunks():
               destination.write(chunk)
           destination.close()

        if myFile2:
           destination = open(os.path.join(filePath, myFile2.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile3:
           destination = open(os.path.join(filePath, myFile3.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile4:
           destination = open(os.path.join(filePath, myFile4.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile5:
           destination = open(os.path.join(filePath, myFile5.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile6:
           destination = open(os.path.join(filePath, myFile6.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        if myFile7:
           destination = open(os.path.join(filePath, myFile7.name),'wb+')
           for chunk in myFile2.chunks():
               destination.write(chunk)
           destination.close()

        filelistStr = ''
        count = 0
        for filename in os.listdir(filePath):
            if filename[0] != '.':
               count = count + 1
               filename = '(%.0f)'  % count + filename + '<br/>'
               filelistStr += filename

        return HttpResponse(text + '<br/>' + 'upload over!<br/>' + 'dir list:<br/>' + filelistStr)

def getUrl1(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text1.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text1.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl2(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text2.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text2.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl3(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text3.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text3.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl4(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text4.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text4.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl5(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text5.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text5.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl6(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text6.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text6.txt not exist' % text)
    else:
        return HttpResponse('please give an name')

def getUrl7(request):
    text = request.GET.get('name')
    if (text):
        filePath = '/Users/wxg/Documents/APIServer/' + text + '/text7.txt'
        if (os.path.exists(filePath)):
            f = open(filePath, 'r')
            text = f.read()
            f.close()
            return HttpResponse(text)
        else:
            return HttpResponse('file %s/text.txt not exist' % text)
    else:
        return HttpResponse('please give an name')


def getcontentstring(request):
    filename = request.GET.get('filename')
    text = getfilecontent(filename)
    return HttpResponse(text)


def writestring(request):
    content = request.POST.get('content')
    foldername = request.POST.get('foldername')
    filename = request.POST.get('filename')
    answer = writecontent(content,foldername,filename)
    return HttpResponse(answer)


def checkfilelist(request):
    name = request.GET.get('foldername')
    text = checkfile(name)
    return HttpResponse(text)

def createforder(request):
    foldername = request.GET.get('foldername')
    text = createfolder(foldername)
    return HttpResponse(text)