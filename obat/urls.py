from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, BookViewSet, SaleViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'books', BookViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = router.urls
