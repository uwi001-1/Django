from rest_framework.routers import DefaultRouter
from ..viewsets.reviews_viewsets import reviewsViewsets

router = DefaultRouter()

router.register('review', reviewsViewsets, basename="reviewsViewsets")