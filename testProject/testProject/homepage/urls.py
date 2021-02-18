from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('pig-game/',views.gameplay, name='pig-game'),
]
