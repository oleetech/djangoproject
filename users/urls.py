from django.urls import path
from .  import views

urlpatterns= [
    path('', views.home, name ='home'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.MylogoutView.as_view(next_page='login'),name='logout'),
]
