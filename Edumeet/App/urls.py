from django.urls import path, re_path
from . import views
app_name = "edu"

urlpatterns = [
    path("home/", views.Home, name="home"),
    re_path(r"video/$", views.Video, name="video"),
    re_path(r"meeting/$", views.Departments, name="meeting")
    
]
