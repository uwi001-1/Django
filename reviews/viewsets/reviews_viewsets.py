from rest_framework import viewsets
from ..models import Reviews
from ..serializers.reviews_serializers import ReviewsListSerializers, ReviewsRetrieveSerializers, ReviewsWriteSerializers

from ..utilities.pagination import MyPageNumberPagination

class reviewsViewsets(viewsets.ModelViewSet):
    serializer_class = ReviewsListSerializers
    queryset = Reviews.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return ReviewsWriteSerializers
        elif self.action == 'retrieve':
            return ReviewsRetrieveSerializers
        return super().get_serializer_class()