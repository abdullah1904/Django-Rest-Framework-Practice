from django.urls import path
from .views import MenuItemsView,MenuItemsViewSet

urlpatterns = [
    # path('menu-item/', MenuItemsView.as_view()),
    # path('menu-item/<int:pk>', SingleMenuItemView.as_view())
    path('menu-item/', MenuItemsViewSet.as_view({'get': 'list','post': 'create'})),
    path('menu-item/<int:pk>',MenuItemsViewSet.as_view({'get': 'retrieve','delete': 'destroy','put': 'update'}))
]