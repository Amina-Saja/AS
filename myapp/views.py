from django.shortcuts import render,redirect
from .models import users

def index(request):
    return render(request,'in.html')

def sign(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')

def sign(request):
    return render(request,'sign.html')

def signin(request):
    if request.method == "POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        username=request.POST['user']
        password=request.POST['psw']
        userdata= users(name=name,email=email,phone=phone,username=username,password=password)
        userdata.save()
        return render(request,'sign.html')
    else:
        return render(request,'sign.html')

def login(request):
    if request.method == "POST":
        username=request.POST['user']
        password=request.POST['pass']
        try:
            logindata=users.objects.get(username=username,password=password)
            return redirect('home.html')
        except users.DoesNotExist:
            return render(request,'login.html',{"status":"Login failed......"})
    else:
        return render(request,'login.html')




