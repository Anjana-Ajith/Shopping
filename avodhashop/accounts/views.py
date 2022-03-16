from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Details')
            return redirect('login')
    else:
        return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')


def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email already taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
                user.save()
                print("User Created")
        else:
            print("Password Not Matched")
        return redirect('/')

    else:
        return render(request,'registration.html')
