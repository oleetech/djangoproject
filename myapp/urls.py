from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('create/',views.order_create,name='order_create'),
    path('order_list/',views.order_list,name='order_list'),
    path('order_update/<int:id>',views.order_update,name='order_update'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),
]