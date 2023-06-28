from django.shortcuts import render
import requests
API_KEY = '3cac7692917746e89fed487749aac232'
# Create your views here.

def home(request):

    country = request.GET.get('country')
    category =request.GET.get('category')
    if country:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()
    else:
        url = f"https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}"
        response = requests.get(url)
        data = response.json()

    articles = data['articles']
    return render(request, "home.html",{"data":data, "articles":articles})

