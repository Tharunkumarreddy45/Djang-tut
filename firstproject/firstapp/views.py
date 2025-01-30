from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def functioncall(request):
    return HttpResponse("Hello World")

def about(request,name,age):
    return HttpResponse("My Name is "+name+" and I am "+str(age)+" years old....")

def call(request,name,num):
    return HttpResponse(name+" with roll number"+str(num))

def page(request):
    return render(request, 'index.html')

def second(request):
    return render(request, 'second.html')

def third(request):
    mydict = {
        'name': "bablu",
        'fruits': ['apple', 'banana', 'orange'],
        'con': False,
        'num1': 55,
        'num2': 16
    }
    return render(request, 'third.html', context=mydict)

def image(request,name):
    myname=name
    myname=myname.lower()
    if myname=='python':
        res=True
    elif name=='django':
        res=False
    else:
        res=None
    mydict={
        'res':res
    }
    return render(request,'image.html',context=mydict)

def form(request):
    return render(request,'form.html')

def submit(request):
    # mydict={
    #     'firstname': request.GET['fname'],
    #     'lastname': request.GET['lname'],
    #     'method': request.method
    # }
    
    mydict={
        'firstname': request.POST['fname'],
        'lastname': request.POST['lname'],
        'method': request.method
    }

    return JsonResponse(mydict)

def reactrendering(request):
    return render(request,'reactproject/build/index.html')