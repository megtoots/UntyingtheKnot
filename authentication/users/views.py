from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('main_page')  # Redirect to main_page upon successful login
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def main_page(request):
    # Logic for rendering the main_page.html template
    return render(request, 'users/main_page.html')
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
def aboutus(request):
    return render(request, 'users/aboutus.html')