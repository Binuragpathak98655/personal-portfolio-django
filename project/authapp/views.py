from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def  signup(request):
    if request.method=="POST":
        get_fname=request.POST.get('fname')
        get_lname=request.POST.get('lname')
        get_password=request.POST.get('pass1')
        get_Retype_Password=request.POST.get('pass2')


        if get_password!=get_Retype_Password:
            messages.info(request,'Password is not matching')
            return redirect('/auth/signup/')
        

        myuser=User.objects.create_user(get_fname,get_lname,get_password)
        myuser.save()
        myuser= authenticate(username=get_fname, password=get_password)
        

        if myuser is not None:
            login(request, myuser)
            messages.success(request,"user is created & Login Success ")
            return redirect('/auth/login/')
    return render(request,'signup.html')

def  handleLogin(request):
    if request.method=="POST":
        get_fname=request.POST.get('fname')
        get_password=request.POST.get('pass1')
        myuser=authenticate(username=get_fname,password=get_password)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success ")
            return redirect('/')
        else:
            messages.error(request,"Login failed")
    return render(request,'login.html')

def  handleLogout(request):
    logout(request)
    messages.success(request,'logout success')
    return render(request,'login.html')