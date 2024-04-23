from django.urls import path
from .views import post_detail,post_list,create_post,update_post,delete_post
from .views2 import Post_list,Post_detail,Post_Delete,Post_Create,Post_update
from .api import PostDetailApi,PostListApi

urlpatterns = [
    path('create',create_post),
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('<int:id>/update',update_post),
    path('<int:id>/delete',delete_post),

    # url to crud operation by cbv

    # path('',Post_list.as_view()),
    # path('<int:pk>',Post_detail.as_view()),
    # path('<int:pk>/create',Post_Create.as_view()),
    # path('<int:pk>/update',Post_update.as_view()),
    # path('<int:pk>/delete',Post_Delete.as_view()),

    # api

    path('api/list',PostListApi.as_view()),
    path('api/list/<int:pk>',PostDetailApi.as_view()),

]
