from django import forms
from .views import Post


class Postform(forms.ModelForm):
    class Meta:
        model=Post
        #fields='__all__'
        exclude=('user',)