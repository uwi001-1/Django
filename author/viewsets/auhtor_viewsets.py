from rest_framework import viewsets
from ..models import Author
from ..serializers.author_serializers import AuthorListSerializers, AuthorRetrieveSerializers, AuthorWriteSerializers

class authorViewsets(viewsets.ModelViewSet):
    serializer_class = AuthorListSerializers
    queryset = Author.objects.all().order_by('-id')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AuthorWriteSerializers
        elif self.action == 'retrieve':
            return AuthorRetrieveSerializers
        return super().get_serializer_class()