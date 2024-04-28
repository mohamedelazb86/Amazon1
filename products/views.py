from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,Brand,Review,ImagProduct


class Product_List(ListView):
    model=Product
    paginate_by=24

class Product_Detail(DetailView):
    model=Product


    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object()).order_by('-id')[:3]
        context["imagess"] = ImagProduct.objects.filter(product=self.get_object())
        context["products"] =Product.objects.filter(brand=self.get_object().brand)

        
        return context
    


class Brand_List(ListView):
    model=Brand

class Brand_detail(DetailView):
    model=Brand

    
