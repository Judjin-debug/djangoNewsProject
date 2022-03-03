from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post
        fields = {
            'time_added': ['gt'],
            'header': ['icontains'],
            'author__user__username': ['icontains'],
        }
