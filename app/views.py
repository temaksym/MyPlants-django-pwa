from django.shortcuts import render, redirect
from django.http import JsonResponse
from app.models import Article, Plant, UserPlant
from django.contrib.auth import logout, authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import timedelta
import random


def index(request):
    return render(request, 'app/index.html')


def plant_list(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('login')
    
    all_plants = Plant.objects.all()
    user_plants = UserPlant.objects.filter(user_id=user.id)
    user_plants_all = list()
    
    for user_plant in user_plants:
        plant = user_plant.plant

        if user_plant.last_watered is None:
            state = "Потрібно полити"
            last_watered = user_plant.last_watered if user_plant.last_watered else "Ніколи"
        elif now() > user_plant.last_watered + timedelta(days=plant.watering_frequency_days):
            state = "Потрібно полити"
            last_watered = user_plant.last_watered.strftime("%Y-%m-%d")
        else:
            state = "Полити через " + str((user_plant.last_watered + timedelta(days=plant.watering_frequency_days) - now()).days) + " днів"
            last_watered = user_plant.last_watered.strftime("%Y-%m-%d")

        user_plants_all.append({
            "id" : user_plant.id,
            "name" : plant.name,
            "description" : plant.description,
            "care_instructions" : plant.care_instructions,
            "watering_frequency_days" : plant.watering_frequency_days,
            "last_watered" : last_watered,
            "state" : state,
        })

    return render(request, 'app/plants.html', {'user_plants': user_plants_all, "all_plants": all_plants})


def add_plant(request):
    user = request.user
    if request.method == 'POST':
        plant_id = request.POST.get('plant_id')
        print(plant_id)
        plant = Plant.objects.get(id=plant_id)
        UserPlant.objects.create(user=user, plant=plant)
    return redirect('plants')


def water(request, plant_id):
    user = request.user
    user_plant = UserPlant.objects.get(id=plant_id, user_id=user.id)
    user_plant.last_watered = now()
    user_plant.save()
    return redirect('plants')


def delete(request, plant_id):
    user = request.user
    user_plant = UserPlant.objects.get(id=plant_id, user_id=user.id)
    user_plant.delete()
    return redirect('plants')


def articles(request):
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