from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts/', views.contacts, name='contacts'),
    
    path('news/', views.news_list, name='news_list'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('news/create/', views.create_news, name='create_news'),
    path('news/<int:news_id>/edit/', views.edit_news, name='edit_news'),
    path('news/<int:news_id>/delete/', views.delete_news, name='delete_news'),
    
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    
]