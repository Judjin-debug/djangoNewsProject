from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple
from .models import Post, Category


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'article_or_news', 'header', 'contents', 'category']

    category = ModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=CheckboxSelectMultiple
    )
