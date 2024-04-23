from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User

class UserSeializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

class Post_listSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    user=UserSeializers()
    class Meta:
        model=Post
        fields='__all__'

class PostDetailSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    user=UserSeializers()
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'

class PostAllSeerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'
