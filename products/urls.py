from django.urls import path
from .views import Product_Detail,Product_List,Brand_List,Brand_detail
from .api import ProductDetailApi,ProductListApi,BrandDetailapi,BrandListApi


urlpatterns = [
    
    path('brands',Brand_List.as_view()),
    path('brands/<slug:slug>',Brand_detail.as_view()),


    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),


     #  api

     path('api/list',ProductListApi.as_view()),
     path('api/list/<int:pk>',ProductDetailApi.as_view()),

     path('api/brand',BrandListApi.as_view()),
     path('api/brand/<int:pk>',BrandDetailapi.as_view()),
]
