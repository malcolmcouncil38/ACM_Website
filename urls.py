# test push
from unicodedata import name
from django.urls import URLPattern, path 
from . import views

urlpatterns = [
  path('', views, name='welcome'),
  path('home/', views.home, name='home'),
  path('GameDev/', views.game, name='game'),
  path('Robotics/', views.robot, name='robot'),
  path('WebDev', views.web, name='web'),
  path('announcements/', views.announce, name='anounce'),
  path('Attendence/', views.attend, name='attend')
]