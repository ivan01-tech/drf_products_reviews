from rest_framework import viewsets
from reviews.models import Product
from reviews.serializers import ProductSerializer
from rest_framework.decorators import action

class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    @action(detail=False)
    def get_list(self, request):
            pass
        
    @action(detail=True)
    def get_product(self, request, pk=None):
        pass