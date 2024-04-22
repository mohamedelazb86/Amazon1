from django.urls import path
from .views import post_detail,post_list,create_post,update_post

urlpatterns = [
    path('create',create_post),
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('<int:id>/update',update_post),
]
