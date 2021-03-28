from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http  import HttpResponse
# Create your views here.

def index(request):
    return render(request,"user/index.html")

def signup(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST.get('password')
        email=request.POST.get('email')
        print(username)
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        userauth=authenticate(username=username,password=password)
        if userauth:
            return render(request,"user/login.html")
        else:
            return HttpResponse(request,"Cant create user")
    return render(request,"user/signup.html")
def view_login(request):
    if(request.method=="POST"):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:    
            login(request,user)
            return render(request,"user/index.html")
        else:
           return  HttpResponse(request,"The account doesnt exist.Please signup")
    return render(request,"user/login.html")
def contact(request):
    return render(request,"user/contact.html")

def booking(request):
    if request.method=="POST":
        date=request.POST["date"]
        return render(request,"user/test.html",{
            "date":date
        })
    return render(request,"user/booking.html")
def test(request):
    date=request.POST["date"]
    
    return render(request,"user/test.html",{
        "date":date
    })
def editbooking(request):
    pass