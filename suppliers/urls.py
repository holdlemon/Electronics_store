from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .apps import SuppliersConfig
from .views import SupplierViewSet, ProductViewSet


app_name = SuppliersConfig.name

router = DefaultRouter()
router.register(r'suppliers', SupplierViewSet)  # Было network
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
