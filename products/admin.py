from django.contrib import admin
from .models import Product,ImagProduct,Review,Brand


class ProductAdmin(admin.ModelAdmin):
    list_display=['name','flag','price','sku']
    list_filter=['brand','flag']
    search_fields=['name','subtitle','descriptions']

    


admin.site.register(Product)
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(ImagProduct)

