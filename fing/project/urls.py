from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories", views.categories, name="categories"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("home", views.all, name="all"),
    path("category/<str:name>", views.filter, name="filter"),
    path("contact", views.contact,name ="contact"),
    path("subscribe", views.subscribe, name="subscribe"),
    path("details/<int:id>", views.details, name="details"),
]