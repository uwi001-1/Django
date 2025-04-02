from rest_framework import serializers
from ..models import Reviews

class ReviewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ReviewsRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'

class ReviewsWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'