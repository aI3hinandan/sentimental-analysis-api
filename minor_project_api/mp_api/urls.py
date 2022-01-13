# api/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('analyze/', views.ApiResponse.as_view()),
    path('watch/', views.Watchlist.as_view()),
    path('register/', views.Register.as_view())
]