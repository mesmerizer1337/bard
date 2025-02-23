from django import forms
from .models import Thread, Post

class ThreadForm(forms.ModelForm):
    """Форма для создания и редактирования темы (Thread)."""
    class Meta:
        model = Thread
        fields = ['name', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название темы'}),
        }

class PostForm(forms.ModelForm):
    """Форма для создания и редактирования постов (Post)."""
    class Meta:
        model = Post
        fields = ['title', 'picture', 'description', 'author']
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Автор'}),
        }
