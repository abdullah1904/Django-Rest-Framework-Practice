from . import views
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# urlpatterns = [
#     path('', views.index),
#     path('login/', views.login),
#     # path('person/',views.person),
#     # path('person/<int:id>',views.singlePerson),
#     path("person/",views.PersonListCreateView.as_view()),
#     path('person/<int:id>',views.PersonDetailView.as_view()),
#     path("personset/", views.PersonViewSet)
# ]

router = DefaultRouter()
router.register(r'person',views.PersonViewSet,basename="person")
urlpatterns = [
    path("", include(router.urls)),
    path("register/", views.Register.as_view()),
    path("login/", views.Login.as_view()),
]