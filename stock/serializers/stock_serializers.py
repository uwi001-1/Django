from rest_framework import serializers
from ..models import Stock

class StockListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'

class StockWriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = '__all__'