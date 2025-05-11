from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Article, Plant, UserPlant

from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import random

def index(request):
    return render(request, 'app/index.html')


def plant_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
        
    user_plants = UserPlant.objects.filter(user_id=user.id)
    user_plants_all = list()

    for user_plant in user_plants:
        plant = user_plant.plant

        if user_plant.last_watered is None:
            state = "Потрібно полити"
            last_watered = user_plant.last_watered if user_plant.last_watered else "Ніколи"
        elif datetime.now() > user_plant.last_watered + timedelta(days=plant.watering_frequency_days):
            state = "Потрібно полити"
            last_watered = user_plant.last_watered.strftime("%Y-%m-%d")
        else:
            state = "Полити через " + str((user_plant.last_watered + timedelta(days=plant.watering_frequency_days) - datetime.now()).days) + " днів"
            last_watered = user_plant.last_watered.strftime("%Y-%m-%d")

        
        user_plants_all.append({
            "name" : plant.name,
            "description" : plant.description,
            "care_instructions" : plant.care_instructions,
            "watering_frequency_days" : plant.watering_frequency_days,
            "last_watered" : last_watered,
            "state" : state,
        })
    return render(request, 'app/plants.html', {'user_plants': user_plants_all})



def add_plant(request):
    return render(request, 'app/add_plant.html')

def water(request, plant_id):
    return redirect('plants')

def delete(request, plant_id):
    # Here you would typically fetch the plant details from the database
    # For now, we'll just pass the plant_id to the template
    return render(request, 'app/delete_plant.html', {'plant_id': plant_id})



def articles(request):
    # Here you would typically fetch the articles from the database
    return render(request, 'app/articles.html')

def article(request, article_id):
    article = Article.objects.get(id=article_id)
    title = article.title
    content = article.content
    created_at = article.created_at
    return render(request, 'app/article.html', {'article_id': article_id, "title": title, "content": content, "created_at": created_at})

def article_list(request):
    articles = list(Article.objects.all())
    data = [{"id": article.id, 'title': article.title, 'content': article.content} for article in articles]
    return JsonResponse(data, safe=False)

def popular_article_list(request):
    articles = list(Article.objects.all())
    random_articles = random.sample(articles, min(len(articles), 3))
    data = [{"id": article.id, 'title': article.title, 'content': article.content} for article in random_articles]
    return JsonResponse(data, safe=False)



def settings(request):
    return render(request, 'app/settings.html')

def profile(request):
    return render(request, 'app/profile.html')

def notifications(request):
    return render(request, 'app/notifications.html')




def login(request):
    return render(request, 'app/login.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            django_login(request, user)
            print("GOOD")
            return redirect('index')
        else:
            print("BAD")
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'app/login.html')
    

def register(request):
    return render(request, 'app/register.html')

def register_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        print(username, password, email)
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')
    else:
        return render(request, 'app/register.html')



def logout_user(request):
    logout(request)
    return redirect('index')