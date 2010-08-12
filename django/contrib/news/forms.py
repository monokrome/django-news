from django import forms
from models import Article

class NewsArticleForm(forms.ModelForm):
    class Meta(object):
        model = Article
        widgets = {
            'body': forms.Textarea(attrs={'class': 'text-edit'}),
        }

