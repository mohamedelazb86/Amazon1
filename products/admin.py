from django.contrib import admin
from .models import Product,ImagProduct,Review,Brand

class Images_product(admin.TabularInline):
    model=ImagProduct

class ProductAdmin(admin.ModelAdmin):
    list_display=['name','flag','price','sku']
    list_filter=['brand','flag']
    search_fields=['name','subtitle','descriptions']

    inlines=[Images_product]




admin.site.register(Product,ProductAdmin)
admin.site.register(Review)
admin.site.register(Brand)
admin.site.register(ImagProduct)

