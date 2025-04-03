from rest_framework.routers import DefaultRouter
from ..viewsets.genre_viewsets import genreViewsets

router = DefaultRouter()

router.register('genre', genreViewsets, basename="genreViewsets")