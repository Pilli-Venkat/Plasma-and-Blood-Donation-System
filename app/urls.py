from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('donate', views.donate,name='donate'),
    path('receive', views.receive,name='receive'),
     path('detail/<slug:title>', views.receive_detail,name='receive_detail'),
    
]