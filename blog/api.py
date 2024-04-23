from .serializers import Post_listSerializers,PostDetailSerializers
from rest_framework import generics
from .models import Post
from .mypaigantion import CustomNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_listSerializers
    pagination_class=CustomNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['draft',]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers

