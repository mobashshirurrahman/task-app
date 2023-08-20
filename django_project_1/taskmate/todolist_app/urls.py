from todolist_app import views
from django.urls import path


urlpatterns = [
    path("", views.todolist, name="todolist"),
    path("todolist", views.todolist, name="todolist"),
    path("contact", views.contact, name="contact"),
    path("about-us", views.about, name="about"),

]