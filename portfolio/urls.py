from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]
