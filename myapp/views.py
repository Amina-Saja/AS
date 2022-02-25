from django.shortcuts import render

def index(request):
    return render(request,'in.html')

def sign(request):
    return render(request,'signup.html')

# Create your views here.
