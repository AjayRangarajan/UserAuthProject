import functools
from django.shortcuts import redirect
from django.contrib import messages

def is_admin_user(view_func, redirect_url="home:home"):
    @functools.wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.groups.filter(name="Admin_Users").exists():
            return view_func(request,*args, **kwargs)
        messages.info(request, "You need to be in Admin group to create normal users")
        return redirect(redirect_url)
    return wrapper
