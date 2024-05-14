from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import UserRegistrationForm 
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()  
    return render(request, 'users/register.html', {'form': form})

def home(request):
    return render(request, 'users/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()  
    return render(request, 'users/login.html', {'form': form})

def main_page(request):
    return render(request, 'users/main_page.html')

def about_us(request):
    return render(request, 'users/aboutus.html')

def educational_materials(request):
    return render(request, 'users/educational_materials.html')

def past_exp(request):
    return render(request, 'users/pastexp.html')

def childhood(request):
    return render(request, 'users/childhood.html')

def currentc(request):
    return render(request, 'users/currentc.html')

def healthandwell(request):
    return render(request, 'users/healthandwell.html')

def rewards(request):
    return render(request, 'users/rewards.html')

def reltech1(request):
    return render(request, 'users/relaxation_techniques1.html')

def reltech2(request):
    return render(request, 'users/relaxation_techniques.html')

def reltech3(request):
    return render(request, 'users/relaxation_techniques2.html')
