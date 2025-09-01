from django.urls import path
from . import views   # this now correctly imports from mytodo/views.py

urlpatterns = [
    path('', views.home, name="home"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('update/<str:pk>/', views.updateTask, name="update"),
]
