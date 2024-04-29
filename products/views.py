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
    paginate_by=24

    

    
    

  
    

# class Brand_detail(DetailView):
#     model=Brand

#     # def get_context_data(self, **kwargs) :
#     #     context = super().get_context_data(**kwargs)
#     #     context["related"] = Product.objects.filter(brand=self.get_object()) 
#     #     return context
    

    
class Brand_detail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    
    def get_queryset(self):
       
       queryset=super().get_queryset().filter(brand__slug=self.kwargs['slug'])
       return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brands"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
   
 
    

    

