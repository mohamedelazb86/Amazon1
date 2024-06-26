from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
FLAG_TYPE=[
    ('New','New'),
    ('Sale','Sale'),
    ('Feature','Feature')
    ]
class Product(models.Model):
    name=models.CharField(max_length=120,verbose_name=_('name'))
    flag=models.CharField(max_length=50,choices=FLAG_TYPE)
    price=models.FloatField()
    image=models.ImageField(upload_to='photo_product')
    sku=models.IntegerField()
    subtitle=models.TextField(max_length=5000)
    descriptions=models.TextField(max_length=50000)
    brand=models.ForeignKey('Brand',related_name='product_brand',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    slug=models.SlugField(null=True,blank=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Product,self).save(*args,**kwargs)
        
    @property
    def review_count(self):
        reviews=self.review_product.all().count()
        return reviews
    
    @property
    def avg_rate(self):
        avg=0
        reviews=self.review_product.all()
        if len(reviews) > 0:
            for review in reviews:
                avg +=review.rate
        else:
            avg=0

        return avg
        

class Brand(models.Model):
    name=models.CharField(max_length=120)
    image=models.ImageField(upload_to='brand_photo')
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super(Brand,self).save(*args,**kwargs)

class ImagProduct(models.Model):
    product=models.ForeignKey(Product,related_name='images_product',on_delete=models.CASCADE)
    images=models.ImageField(upload_to='images')

    def __str__(self):
        return str(self.product)
    
class Review(models.Model):
    product=models.ForeignKey(Product,related_name='review_product',on_delete=models.SET_NULL,null=True,blank=True)
    user=models.ForeignKey(User,related_name='review_user',on_delete=models.CASCADE)
    content=models.TextField(max_length=1000)
    rate=models.IntegerField(choices=[(i,i) for i in range(1,6)])
    publish_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.product}---{self.user}"
    

