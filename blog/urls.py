from django.urls import path
from .  import views 

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('posts/',views.PostList.as_view(),name='posts'),
    path('post/<int:pk>/',views.PostDetails.as_view(),name='post'),
    path('post/create/',views.CreateView.as_view(),name='post-create'),
    path('post/update/<int:pk>',views.PostUpdate.as_view(),name='post-update'),
    path('post/<int:pk>/delete',views.PostDelete.as_view(),name='post-delete')

]