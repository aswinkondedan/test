from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
from .serializers import Appser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse



# def createfunction(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         age=request.POST['age']
#         contact=request.POST['contact']
#         register=student(name=name,age=age,contact=contact)
#         register.save()
#     getdata=student.objects.all()
#     return render (request,'create.html',{'res':getdata})
# def deletefunction(request,id):
#     student.objects.get(id=id).delete()
#     return redirect ('create')

# def updatefunction(request,id):
#     update=student.objects.get(id=id)
#     return render (request,'update.html',{'editprof':update})

# def updationfunction(request,id):
#     if request.method=="POST":
#         name=request.POST['name']
#         age=request.POST['age']
#         contact=request.POST['contact']
#         student.objects.filter(id=id).update(name=name,age=age,contact=contact)
#     return redirect ('create')

# def viewfunction(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         contact=request.POST['contact']
#         place=request.POST['place']
#         image=request.FILES['image']
#         #print(image.name)
#         #print (random()) #to generate number for each
#         img=str(random())+image.name 
#         #print (img)
#         obj=FileSystemStorage()
#         obj.save(img,image)
#         pic=picture(name=name,contact=contact,place=place,image=img)
#         pic.save()
#     return render (request,'view.html')

# def showfunction(request):
#     show=picture.objects.all()
#     return render (request,'show.html', {'k':show})


@csrf_exempt
def datafunction(request,id=0):
    if request.method=='POST':
        userdata=JSONParser().parse(request)
        user_serializer=Appser(data=userdata)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse('data inserted succesfully',safe=False)
        return JsonResponse('failed to register',safe=False)

    elif request.method=='GET':
        user=details.objects.all()
        user_serializer=Appser(user,many='True')
        return JsonResponse(user_serializer.data,safe=False)

    elif request.method=='DELETE':
        user=details.objects.get(id=id)
        user.delete()
        return JsonResponse('data deleted',safe=False)

    elif request.method=='PUT':
        userdata=JSONParser().parse(request)
        user=details.objects.get(id=userdata['id'])
        user_serializer=Appser(user,userdata)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse ('data updated',safe=False)
        return JsonResponse ('failed',safe=False)  
    






