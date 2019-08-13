from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required



def home_view(request):
    return render(request,'Home.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['emailid'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect('home')
        else:
            messages.error(request, 'invalid user_name/Password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['emailid']).exists():
            messages.error(request, 'User is alredy registered?')
            return render(request, 'register.html')
        else:
            if request.POST['password'] == request.POST['confirmpassword']:
                user = User()
                user.name = request.POST['name']
                user.email = request.POST['emailid']
                user.username = request.POST['emailid']
                user.mobile_no = request.POST['mobile']
                user.password = make_password(request.POST['password'])
                user.save()

                messages.success(request, 'User is Registered successfully?')
                return redirect('login')
            else:
                messages.error(request, "password and confirm password did'nt match")
                return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')
