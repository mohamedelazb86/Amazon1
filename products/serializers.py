from rest_framework import serializers
from .models import Product,Brand

class ProductListSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'
class ProductDetailSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Product
        fields='__all__'


class BrandListSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Brand
        fields='__all__'

class BrandDetailSerializers(serializers.ModelSerializer):
    brand=serializers.StringRelatedField()
    class Meta:
        model=Brand
        fields='__all__'

