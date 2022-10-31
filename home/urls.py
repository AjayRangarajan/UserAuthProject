from django.urls import path
from . import views


app_name = "home"


urlpatterns = [
    path("", views.home, name="home"),
    path("create_admin_user/", views.create_admin_user, name="create_admin_user"),
    path("admin_user_login/", views.admin_user_login, name="admin_user_login")
]

