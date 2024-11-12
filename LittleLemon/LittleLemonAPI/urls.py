from django.urls import path
from .views import MenuItemsView,MenuItemsViewSet
from rest_framework.authtoken.views import obtain_auth_token 

urlpatterns = [
    # path('menu-item/', MenuItemsView.as_view()),
    # path('menu-item/<int:pk>', SingleMenuItemView.as_view())
    path('menu-item/', MenuItemsViewSet.as_view({'get': 'list','post': 'create'})),
    path('menu-item/<int:pk>',MenuItemsViewSet.as_view({'get': 'retrieve','delete': 'destroy','put': 'update'})),
    # path('secret/',secret),
    # path('me',me),
    # path('manager',manager_view),
    path('getToken',obtain_auth_token),
]