from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='autohome'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    
]