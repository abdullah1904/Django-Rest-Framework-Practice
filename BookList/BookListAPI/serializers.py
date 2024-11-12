from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    author_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = Book
        fields = ['id','title','price','author','author_id']
    def validate_author_id(self, author_id):
        if not Author.objects.filter(id=author_id).exists():
            raise serializers.ValidationError("Author does not exist.")
        return author_id
