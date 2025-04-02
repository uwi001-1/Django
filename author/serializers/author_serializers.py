from rest_framework import serializers
from ..models import Author

class AuthorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class AuthorWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'