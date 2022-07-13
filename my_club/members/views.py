from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterUserForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def change_password(request):
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request,("Your password was successfully updated!"))
            return redirect('home')
        else:
            messages.error(request,'Please correct the error below.')
    else:
        form = ChangePasswordForm(request.user)
    
    return render(request, 'registration/change_password.html',
    {"form":form})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))
            return redirect('login')
    else:
        return render(request, 'registration/login.html',{})

def logout_user(request):
    logout(request)
    messages.success(request, ("Logout Successfully"))
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request,("Regitered Successfully"))
            return redirect('home')
    else:
        form = RegisterUserForm()
    return render(request, 'registration/register.html',
    {'form': form})