from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from home.models import User

def home(request):
    return HttpResponse("Welcome to the home page.")


@staff_member_required
def create_admin_user(request):
    if request.method == 'POST':
        form = AdminUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            admin_users = Group.objects.get(name='Admin_Users') 
            admin_users.user_set.add(user)
            messages.success(request, f'{username} created Succcessfully!')
            return redirect('home:admin_user_login')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('home:create_admin_user')
    form = AdminUserRegistrationForm()
    context = {
        'title': 'Admin User Registration Page',
        'form': form,
    }
    return render(request, 'home/create_admin_user.html', context)

def admin_user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        admin_key = request.POST.get('admin-key')
        user = authenticate(username=username, password=password)
        if user != None and User.objects.filter(auth_key=admin_key).first():
            login(request, user)
            messages.success(request, f'successfully logged in as {username}')
            return redirect('home:home')
        else:
            messages.error(request, 'Invalid credentials!')
            return redirect('home:admin_user_login')
    context = {
        'title': "ADMIN USER LOGIN",
    }
    return render(request, 'home/admin_user_login.html', context)