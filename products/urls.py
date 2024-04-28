from django.urls import path
from .views import Product_Detail,Product_List,Brand_List,Brand_detail


urlpatterns = [
    
    path('brands',Brand_List.as_view()),
    path('brands/<slug:slug>',Brand_detail.as_view()),


    path('',Product_List.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
]
