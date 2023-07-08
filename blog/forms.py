from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'location',
            'desc',
            'category',
            'latitude',
            'longitude',
            'image',
            'author_name',
            'author_id',
            ]