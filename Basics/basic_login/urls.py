from django.urls import path
from . import views

urlpatterns = [
    path("login_page.html", views.login_page, name='login_page'),
    path("", views.landing_page, name ='landing_page'),


]