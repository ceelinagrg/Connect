from django.core import validators
from django import forms
from .models import Post

class UserPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content', 'image']
        # widgets = {
        #     'author': forms.TextInput,
        #     'title': forms.TextInput,
        #     'content': forms.TextInput,
        #     'image': forms.ImageField
        # }