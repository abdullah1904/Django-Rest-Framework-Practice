from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'author',views.AuthorViewSet,basename="author")
router.register(r'book',views.BookViewSet,basename="book")

urlpatterns = [
    path('',include(router.urls))
]