from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from models import *
# from news.models import * --- for shell


u1 = User.objects.create_user(username='username1')
u2 = User.objects.create_user(username='username2')
u3 = User.objects.create_user(username='username3')

a1 = Author.objects.create(user=u1)
a2 = Author.objects.create(user=u2)

cat1 = Category.objects.create(category_name='Politics')
cat2 = Category.objects.create(category_name='Military')
cat3 = Category.objects.create(category_name='Industry')
cat4 = Category.objects.create(category_name='Environment')

p1 = Post.objects.create(author=a1, article_or_news='A', header='Clickbait1', contents='00 1234567'
                                                                                       '01 1234567'
                                                                                       '02 1234567'
                                                                                       '03 1234567'
                                                                                       '04 1234567'
                                                                                       '05 1234567'
                                                                                       '06 1234567'
                                                                                       '07 1234567'
                                                                                       '08 1234567'
                                                                                       '09 1234567'
                                                                                       '10 1234567'
                                                                                       '11 1234567'
                                                                                       '12 1234567'
                                                                                       '13 1234567')
p2 = Post.objects.create(author=a1, article_or_news='A', header='Clickbait2', contents='Snow caps will melt')
p3 = Post.objects.create(author=a2, article_or_news='N', header='Clickbait3', contents='We are all doomed')


p1.category.add(cat3)
p2.category.add(cat4)
p3.category.add(cat1, cat2)

comm1 = Comment.objects.create(post=p1, user=u3, contents='First')
comm2 = Comment.objects.create(post=p2, user=u3, contents='First')
comm3 = Comment.objects.create(post=p3, user=u3, contents='First')
comm4 = Comment.objects.create(post=p3, user=u1, contents='So much for disarmament trend')

comm1.dislike()
comm1.dislike()

comm2.dislike()
comm2.dislike()

comm3.dislike()
comm3.dislike()

comm4.like()
p3.like()

a1.update_rating()
a2.update_rating()

print(Author.objects.order_by('-rating').values('user__username', 'rating')[0])

print(dict((Post.objects.order_by('-rating').values('time_added', 'author__user__username', 'rating', 'header')[0]),
      **dict(preview=Post.objects.order_by('-rating')[0].preview)))

print(Comment.objects.filter(post=Post.objects.order_by('-rating')[0]).values('time_added', 'user__username', 'rating', 'contents'))







