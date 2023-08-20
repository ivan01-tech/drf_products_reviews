from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("reviews.urls")),
    path("token/", TokenObtainPairView.as_view(), name="token"),
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),
    # path("verify/", TokenObtainPairView.as_view(), name="verify"),
]

# to serve static files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
