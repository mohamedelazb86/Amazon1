from .serializers import ProductDetailSerializers,ProductListSerializers
from .serializers import BrandDetailSerializers,BrandListSerializers
from .models import Brand,Product
from rest_framework import generics


class ProductListApi(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductListSerializers

class ProductDetailApi(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductDetailSerializers

class BrandListApi(generics.ListAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandListSerializers

class BrandDetailapi(generics.RetrieveAPIView):
    queryset=Brand.objects.all()
    serializer_class=BrandDetailSerializers


    