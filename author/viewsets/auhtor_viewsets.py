from rest_framework import viewsets
from ..models import Author
from ..serializers.author_serializers import AuthorListSerializers, AuthorRetrieveSerializers, AuthorWriteSerializers

from ..utilities.pagination import MyPageNumberPagination
# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

class authorViewsets(viewsets.ModelViewSet):
    serializer_class = AuthorListSerializers
    queryset = Author.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination
    # permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return AuthorWriteSerializers
        elif self.action == 'retrieve':
            return AuthorRetrieveSerializers
        return super().get_serializer_class()