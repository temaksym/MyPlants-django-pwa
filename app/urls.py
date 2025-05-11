from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('articles/', views.articles, name='articles'),
    path('api/popular_articles/', views.popular_article_list, name='popular_article_list'),
    path('api/articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article, name='article'),

    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),

    path('plants/', views.plant_list, name='plants'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('delete/<int:plant_id>/', views.delete, name='delete'),
    path('water/<int:plant_id>/', views.water, name='water'),

    path('login/', views.login, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
]