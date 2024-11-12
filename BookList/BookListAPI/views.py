from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import generics, viewsets


class AuthorViewSet(viewsets.ModelViewSet):
    model = Author
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    ordering_fields = ['name','country']
    search_fields = ['name']

class BookViewSet(viewsets.ModelViewSet):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    ordering_fields = ['title','price']
    search_fields = ['title']
