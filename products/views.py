from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Product,Brand


class Product_List(ListView):
    model=Product

class Product_Detail(DetailView):
    model=Product

class Brand_List(ListView):
    model=Brand

class Brand_detail(DetailView):
    model=Brand

    
