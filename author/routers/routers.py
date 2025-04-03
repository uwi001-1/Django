from rest_framework.routers import DefaultRouter
from ..viewsets.auhtor_viewsets import authorViewsets

router = DefaultRouter()

router.register('author', authorViewsets, basename="authorViewsets")