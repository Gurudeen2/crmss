from django.shortcuts import redirect, render
from .models import Account
from django.contrib import messages
from CRMS.sessionFunc import sessions
from datetime import datetime


# Create your views here.
def index(request):
    # sessions(request)
    username= request.session["username"]
    if not username:
        messages.error(request, "Session Expired")
        return redirect('login')
    else:
        acc = Account.objects.filter(username=username)
    return render(request, "pages/index.html", {'dashboards':acc})

def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password = request.POST['passwrd']
    
        # request.session['last_activity'] = datetime
        auth = Account.objects.filter(username=username, passowrd=password) or Account.objects.filter(email=username, passowrd=password)
        if auth.exists():
            request.session["username"] = username 
            request.session["last_login"] = str( datetime.now())

            messages.success(request, "Login Successful")
            return redirect('dashboard')
        if Account.objects.filter(username=username).exists() or Account.objects.filter(email=username).exists():
            messages.error(request, "Invalid Password")
            return redirect("login")
        if Account.objects.filter(passowrd=password).exists():
            messages.error(request, "Invalid Username")
            return redirect("login")
        if not auth.exists():
            messages.error(request, "Invalid Username and Password")
            return redirect("login")
    return render(request, 'accounts/login.html')
def charToAscii(param):
    c= ''
    for i in param:
        ordco = ord(i)
        c += str(ordco)
    return c[:8]
    
def register(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        middlename = request.POST['mname']
        lastname = request.POST['lname']
        username = request.POST['username']
        email = request.POST['uemail']
        conpassword = request.POST['conpasswrd']
        password = request.POST['passwrd']
        if conpassword == password:
            id = lastname.lower()+'-'+charToAscii(firstname.lower())
            checkUser = Account.objects.filter(username=username)
            if checkUser.exists():
                messages.error(request, 'Username already exist')
                return redirect("register")
            if Account.objects.filter(email=email).exists():
                messages.error(request, "Email Already Exist")
                return redirect("register")
            else:

                regUser = Account.objects.create(userid = id, firstname = firstname, middlename = middlename,
                    lastname = lastname, username = username, email = email, passowrd = password)
                regUser.save()
                messages.success(request, "Registration Success")
                return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'alert':'Password do not match'})
    return render(request, 'accounts/register.html')

def logout(request):
    return render(request, "accounts/login.html")