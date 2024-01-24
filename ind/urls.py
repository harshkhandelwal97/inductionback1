from django.urls import path
from . import views
 
urlpatterns =[
    path('log/',views.log),
    path('home/',views.home),
    path('progress/',views.progress),
    path('comments/',views.comment),
 
]