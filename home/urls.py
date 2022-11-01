from django.urls import path
from . import views


app_name = "home"


urlpatterns = [
    path("", views.home, name="home"),
    path("create_admin_user/", views.create_admin_user, name="create_admin_user"),
    path("user_login/", views.user_login, name="user_login"),
    path("create_normal_user/", views.create_normal_user, name="create_normal_user"),
]

