from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('plant_list/', views.plant_list, name='plant_list'),
    path('plant_detail/<int:plant_id>/', views.plant_detail, name='plant_detail'),
    path('add_plant/', views.add_plant, name='add_plant'),
    path('edit_plant/<int:plant_id>/', views.edit_plant, name='edit_plant'),
    path('delete_plant/<int:plant_id>/', views.delete_plant, name='delete_plant'),

    path('articles/', views.articles, name='articles'),
    path('api/popular_articles/', views.popular_article_list, name='popular_article_list'),
    path('api/articles/', views.article_list, name='article_list'),
    path('article/<int:article_id>/', views.article, name='article'),

    path('settings/', views.settings, name='settings'),
    path('profile/', views.profile, name='profile'),
    path('notifications/', views.notifications, name='notifications'),

    path('plants/', views.plant_list, name='plants'),
    path('plant/<int:plant_id>/', views.plant_detail, name='plant_detail'),

    path('login/', views.login, name='login'),
    path('login_user', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('logout/', views.logout_user, name='logout'),
]