from rest_framework.routers import DefaultRouter
from reviews.views import ProductViewSet
from django.urls import include

router = DefaultRouter()
router.register("produts", ProductViewSet)
urlpatterns = [
    # include("", router.urls),
]

urlpatterns += router.urls
