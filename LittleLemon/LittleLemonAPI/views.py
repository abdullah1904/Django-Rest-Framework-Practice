from rest_framework import generics, filters,status, viewsets
from rest_framework.response import Response
from .models import MenuItem
from django_filters.rest_framework import DjangoFilterBackend, FilterSet, NumberFilter, CharFilter
from .serializers import MenuItemSerializer
from django.core.paginator import Paginator, EmptyPage
from .paginations import CustomMenuItemPagination

class MenuItemFilter(FilterSet):
    category = CharFilter(field_name="category__title", lookup_expr="exact")  # Filter by category (case insensitive)
    to_price = NumberFilter(field_name="price", lookup_expr="lte")      # Filter for price <= to_price

    class Meta:
        model = MenuItem
        fields = ['category', 'to_price']


class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = MenuItemFilter
    ordering_fields = ['price','title']
    ordering = ['title']
    pagination_class = CustomMenuItemPagination
    # def get(self,request):
    #     data = MenuItem.objects.all()
    #     category = request.query_params.get('category',None)
    #     to_price = request.query_params.get('to_price',None)
    #     search = request.query_params.get('search',None)
    #     ordering = request.query_params.get('ordering',None)
    #     perpage = request.query_params.get('perpage',2)
    #     page = request.query_params.get('page',1)
    #     if search:
    #         # data = data.filter(title__startswith=search)
    #         # data = data.filter(title__icontains=search)
    #         data = data.filter(title__contains=search)
    #     if category:
    #         data = data.filter(category__title=category)
    #     if to_price:
    #         data = data.filter(price__lte=to_price)
    #     if ordering:
    #         ordering_fields = ordering.split(',')
    #         data = data.order_by(*ordering_fields)
    #     paginator = Paginator(data,per_page=perpage)
    #     try:
    #         data = paginator.page(number=page)
    #     except EmptyPage:
    #         data = []
    #     data = MenuItemSerializer(data,many=True)
    #     return Response(data.data,status=status.HTTP_200_OK)

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    ordering_fields=['price','inventory']
    search_fields=['title','category__title']