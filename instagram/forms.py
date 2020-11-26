from django import forms
from .models import Image

class PostImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image_name','caption']