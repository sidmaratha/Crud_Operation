from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('add', views.add, name='add'),
    path('show', views.show, name='show'),
    path('', views.ShowDetailsPage, name='ShowDetailsPage'),
    path('EditPage/<id>', views.EditPage, name='EditPage'),
    path('SaveEdit', views.SaveEdit, name='SaveEdit'),
    path('ConfirmDelete/<id>', views.ConfirmDelete, name='ConfirmDelete'),
]