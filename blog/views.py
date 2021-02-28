from rest_framework.generics import (
    CreateAPIView, RetrieveAPIView, ListAPIView, DestroyAPIView
)
from .models import Product
from .serializers import ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
