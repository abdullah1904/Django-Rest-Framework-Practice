from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index),
    path('login/', views.login),
    path('person/',views.person),
    path('person/<int:id>',views.singlePerson),
]