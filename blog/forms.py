from django import forms
from .models import Comments

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'content')
        widgets = {
            "name": forms.TextInput(attrs={'class': 'col-sm-12'}),
            "email": forms.TextInput(attrs={'class': 'col-sm-12'}),
            "content": forms.TextInput(attrs={'class': 'col-sm-12'}),
        }