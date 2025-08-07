from django import forms
from .models import Comments
from mptt.forms import TreeNodeChoiceField



class NewCommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comments.objects.all())
    # будет требовать выбрать родителя для комментария

    def __init__(self, *args, **kwargs): # даёт доступ не выбрать родителя
        super().__init__(*args, **kwargs)
        self.fields['parent'].widget.attrs.update(
            {'class': 'd-none'}
        )
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comments
        fields = ('name','parent','email', 'content')
        widgets = {
            "name": forms.TextInput(attrs={'class': 'col-sm-12'}),
            "email": forms.TextInput(attrs={'class': 'col-sm-12'}),
            "content": forms.TextInput(attrs={'class': 'col-sm-12'}),
        }