from rest_framework import serializers
from ..models import Book
from genre.models import Genre
from author.models import Author

class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'genre_name']
        ref_name = 'genre_book'

class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author_name']

class BookListSerializers(serializers.ModelSerializer):
    genre = GenreSerializers(read_only = True)
    author = AuthorSerializers(read_only = True)
    class Meta:
        model = Book
        fields = ['id', 'slug', 'title', 'genre', 'author']

class BookRetrieveSerializers(serializers.ModelSerializer):
    genre = GenreSerializers(read_only = True)
    class Meta:
        model = Book
        fields = '__all__'

class BookWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

def create(self, validated_data):  #Overwrite CREATE
    return super().create(validated_data)

def update(self, instance, validated_data):
    return super().update(instance, validated_data)