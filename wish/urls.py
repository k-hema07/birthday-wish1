from django.urls import path
from . import views
urlpatterns = [
    path('', views.lock, name='lock'),
    path('wish/', views.wish, name='wish'),
    path('logout/', views.logout, name='logout'),
    path('sw.js', views.sw, name='sw'),
]
