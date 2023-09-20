from django import forms
from . import models

class CreateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'slug', 'body', 'thumb']
        
class UpdateBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = ['title', 'slug', 'body', 'thumb']