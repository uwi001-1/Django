from rest_framework import serializers
from ..models import Genre

class GenreListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class GenreWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'