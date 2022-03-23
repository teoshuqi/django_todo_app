from django.contrib import admin
from django.urls import path, include
from. import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new-todo', views.newToDo, name="new_todo"),
    path('mark-as-done/<int:id>', views.markAsDone, name="mark_as_done"),
]