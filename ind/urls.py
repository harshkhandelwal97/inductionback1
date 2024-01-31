# urls.py
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html', success_url='ind/home/'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('log/',views.log , name = 'login'),
    path('home/', views.home, name='home'),
    path('progress/', views.progress, name='progress'),
    path('comments/', views.comment, name='comments'),
    path('redirect_to_progress/', views.redirect_to_progress, name='redirect_to_progress'),
    path('saveprogress/', views.saveprogress, name='saveprogress'),
    path('logged/',views.logged,name ='logged')
    
    # path('home/', views.login_view, name='home'),
]

