from rest_framework import viewsets
from reviews.models import Product
from reviews.serializers import ProductSerializer
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerailizer




class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated,]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ("category",)
    permit_list_expands = [
        "category",
        "sites",
        "comments",
        "sites.company",
        "sites.productsize",
    ]

    @action(detail=False)
    def get_list(self, request):
        pass

    @action(detail=True)
    def get_product(self, request, pk=None):
        pass
