from django.shortcuts import render

def index(request):
    return render(request,'in.html')

def sign(request):
    return render(request,'signup.html')

def sign(request):
    return render(request,'sign.html')

def signin(request):
    if request.method == "POST":
        name=request.post['name']
        email=request.post['email']
        phone=request.post['phone']
        username=request.post['username']
        password=request.post['password']
        userdata= user(name=name,email=email,phone=phone,username=username,password=password)
        userdata.save()
        return render(request,'sign.html')
    else:
         return render(request,'sign.html')



