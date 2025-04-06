from rest_framework import viewsets
from ..models import Genre
from ..serializers.genre_serializers import GenreListSerializers, GenreRetrieveSerializers, GenreWriteSerializers

from utilities.pagination import MyPageNumberPagination

class genreViewsets(viewsets.ModelViewSet):
    serializer_class = GenreListSerializers
    queryset = Genre.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GenreWriteSerializers
        elif self.action == 'retrieve':
            return GenreRetrieveSerializers
        return super().get_serializer_class()