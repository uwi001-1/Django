from rest_framework.routers import DefaultRouter
from ..viewsets.book_viewsets import bookViewsets

router = DefaultRouter()

router.register('book', bookViewsets, basename="bookViewsets")