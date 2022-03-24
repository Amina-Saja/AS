from django.shortcuts import render,redirect
from .models import users

def index(request):
    return render(request,'in.html')

def sign(request):
    return render(request,'signup.html')

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def register(request):
    return render(request,'register.html')

def cologin(request):
    return render(request,'cologin.html')
    
def admin(request):
    return render(request,'admin.html')

def emp(request):
    return render(request,'emp.html')

def sign(request):
    return render(request,'sign.html')

def register(request):
    if request.method == "POST":
        name=request.POST['name']
        place=request.POST['place']
        email=request.POST['email']
        address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirm']
        userdata= users(name=name,place=place,email=email, address=address,username=username,password=password,confirmpassword=confirmpassword)
        userdata.save()
        return render(request,'register.html')
    else:
        return render(request,'register.html')

def signin(request):
    if request.method == "POST":
        name=request.POST['name']
        place=request.POST['place']
        email=request.POST['email']
        address=request.POST['address']
        username=request.POST['username']
        password=request.POST['password']
        confirm=request.POST['confirm']
        userdata= users(name=name,place=place,email=email, address=address,username=username,password=password,confirm=confirm)
        userdata.save()
        return render(request,'register.html')
    else:
        return render(request,'register.html')
        
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




