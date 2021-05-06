from django.shortcuts import render, redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,'home_page.html')

def top_picks(request):
    context = {
        'picks' : TopPicks.objects.all()
    }
    return render(request,'top_picks.html', context)

def best_sellers(request):
    context = {
        'bsellers' : BestSeller.objects.all()
    }
    return render(request, "best_sellers.html", context)

def new_arrivals(request):
    context = {
        "arrivals" : NewArrivals.objects.all()
    }
    return render(request, "new_arrivals.html", context)

def return_home(request):
    return redirect('/')