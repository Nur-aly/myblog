from django.forms import ModelForm
from .models import Comment
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control", "id": "name", 'placeholder': 'Имя'}),
            'body': forms.Textarea(attrs={'id': "message", 'cols': "30", 'class': "form-control"}),
        }
