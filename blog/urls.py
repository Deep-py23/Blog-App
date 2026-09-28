
from django.urls import path
from . import views

urlpatterns = [
    
    path('<int:pk>/', views.view_post, name='view_post'),
    path('add/', views.add_post, name='add_post'),
    path('update/<int:pk>/', views.update_post, name='update_post'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    
]