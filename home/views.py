from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from home.models import User
from home.decorators import *

def home(request):
    return render(request, 'home/home.html')


@staff_member_required
def create_admin_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = User.objects.filter(username=username).first()
            admin_users = Group.objects.get(name='Admin_Users') 
            admin_users.user_set.add(user)
            messages.success(request, f'{username} created Succcessfully!')
            return redirect('home:user_login')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('home:create_admin_user')
    form = UserRegistrationForm()
    context = {
        'title': 'Admin User Registration Page',
        'form': form,
    }
    return render(request, 'home/create_user.html', context)


def user_login(request):
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
            return redirect('home:user_login')
    context = {
        'title': "USER LOGIN",
    }
    return render(request, 'home/user_login.html', context)

@login_required
@is_admin_user
def create_normal_user(request):
    if request.method == 'POST':
        form = NormalUserRegistrationForm(request.POST)
        if form.is_valid():
            auth_key = request.user.auth_key
            users = User.objects.filter(auth_key=auth_key).all()
            if len(users) > 5:
                messages.error(request, 'User creation limit exceeded for this Admin')
                return redirect('home:home')
            user = form.save()
            user.auth_key = auth_key
            user.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} created Succcessfully!')
            return redirect('home:user_login')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('home:create_normal_user')
    form = NormalUserRegistrationForm()
    context = {
        'title': 'Admin User Registration Page',
        'form': form,
        'view': 'create_normal_user',
    }
    return render(request, 'home/create_user.html', context)