from django.urls import path
from . import views

urlpatterns = [path('', views.index, name="Ex00 Markdown cheatsheet"),]
