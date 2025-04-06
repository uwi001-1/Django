from rest_framework import viewsets
from ..models import Book
from ..serializers.book_serializers import BookListSerializers, BookRetrieveSerializers, BookWriteSerializers

from utilities.pagination import MyPageNumberPagination

class bookViewsets(viewsets.ModelViewSet):
    serializer_class = BookListSerializers
    queryset = Book.objects.all().order_by('-id')
    pagination_class = MyPageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return BookWriteSerializers
        elif self.action == 'retrieve':
            return BookRetrieveSerializers
        return super().get_serializer_class()
    