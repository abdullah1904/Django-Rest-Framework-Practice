from django.urls import path
from .views import MenuItemsView,SingleMenuItemView

urlpatterns = [
    path('menu-item/', MenuItemsView.as_view()),
    path('menu-item/<int:pk>', SingleMenuItemView.as_view())
]