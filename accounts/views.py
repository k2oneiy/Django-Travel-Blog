from django.shortcuts import render , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect("/")
        else:
            messages.info(request, "inVaild details")
            return redirect("login")
    else:
        return render(request,"login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST['userfirstname']
        last_name = request.POST['userlastname']
        user_name = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        subject = 'welcome to travello'
        message = f'Hi {first_name}, thank you for registering in travello.'
        email_from = 'iyappanhacker@gmail.com'
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )    



        if password1==password2:
            user = User.objects.create_user(username=user_name,password=password1,email=email,first_name=first_name,last_name=last_name)
            user.save()
            print("User Created ......")
            return redirect('login')
        else:
            messages.info(request,"Password Not Match ")
            print("password Not matching")    

    else:
        return render(request,"register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')