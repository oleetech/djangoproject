from django.urls import path
from . import views

urlpatterns =[
    path('',views.create_quiz,name='create_quiz'),
    path('quiz_list',views.quiz_list,name='quiz_list'),
    path('quiz_detail/<int:id>',views.quiz_detail,name='detail_quiz'),
    path('edit_quiz/<int:id>',views.edit_quiz,name='edit_quiz'),
    path('delete_quiz/<int:id>',views.delete_quiz,name='delete_quiz'),

    path('create_quistion/<int:id>',views.create_quistion,name='create_quistion')
    

]