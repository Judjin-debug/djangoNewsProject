from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from datetime import datetime


class Author(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        total_sum = (Post.objects.filter(author=self).aggregate(Sum('rating')).get('rating__sum') or 0) * 3 + \
                    (Comment.objects.filter(user=self.user).aggregate(Sum('rating')).get('rating__sum') or 0) + \
                    (Comment.objects.filter(post__author=self).aggregate(Sum('rating')).get('rating__sum') or 0)
        self.rating = total_sum
        self.save()


class Category(models.Model):

    category_name = models.CharField(max_length=255, unique=True)


class Post(models.Model):

    news = 'N'
    article = 'A'

    CONTENT_TYPE = [
        (news, 'News'),
        (article, 'Article')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article_or_news = models.CharField(max_length=1, choices=CONTENT_TYPE, default=article)
    header = models.CharField(max_length=255)
    contents = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    category = models.ManyToManyField(Category, through='PostCategory')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    @property
    def preview(self):
        return self.contents[:124]


class PostCategory(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contents = models.TextField()
    time_added = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
