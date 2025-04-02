from rest_framework import viewsets
from ..models import Stock
from ..serializers.stock_serializers import StockListSerializers, StockRetrieveSerializers, StockWriteSerializers

class bookViewsets(viewsets.ModelViewSet):
    serializer_class = StockListSerializers
    queryset = Stock.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return StockWriteSerializers
        elif self.action == 'retrieve':
            return StockRetrieveSerializers
        return super().get_serializer_class()