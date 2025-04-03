from rest_framework.routers import DefaultRouter
from ..viewsets.stock_viewsets import stockViewsets

router = DefaultRouter()

router.register('stock', stockViewsets, basename="stockViewsets")