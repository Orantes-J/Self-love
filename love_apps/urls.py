from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('toppicks', views.top_picks),
    path('bestsellers', views.best_sellers),
    path('newarrivals', views.new_arrivals),
    path('return', views.return_home),
]