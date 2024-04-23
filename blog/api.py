from .serializers import Post_listSerializers,PostDetailSerializers
from rest_framework import generics
from .models import Post


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_listSerializers

class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=PostDetailSerializers

    