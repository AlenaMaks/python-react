from django import forms
from .models import Comment
from .models import News

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        
class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'image_url']