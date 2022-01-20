from django import forms
from .models import Blog


class NewsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'text', 'category', 'image', 'author',
                  'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'image' : forms.FileInput(attrs={'class': 'form-control'}),
        }