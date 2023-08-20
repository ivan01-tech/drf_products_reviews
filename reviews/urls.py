from rest_framework.routers import DefaultRouter
from reviews.views import ProductViewSet

router = DefaultRouter()
router.register("produts", ProductViewSet)

urlpatterns = [
    
]

urlpatterns += router.urls
