from django.urls import path
from . import views
urlpatterns = [
    
    path('', views.citizen_list,name='citizen_list'),
    path('add_citizen/', views.add_citizen,name='add_citizen'),
    path('update_citizen/<int:id>', views.update_citizen,name='update_citizen'),
    path('delete_citizen/<int:id>', views.delete_citizen,name='delete_citizen'),
]