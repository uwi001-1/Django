from rest_framework import viewsets
from ..models import Genre
from ..serializers.genre_serializers import GenreListSerializers, GenreRetrieveSerializers, GenreWriteSerializers

class genreViewsets(viewsets.ModelViewSet):
    serializer_class = GenreListSerializers
    queryset = Genre.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GenreWriteSerializers
        elif self.action == 'retrieve':
            return GenreRetrieveSerializers
        return super().get_serializer_class()