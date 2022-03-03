from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from .models import Author, Category, Post, PostCategory, Comment
from .filters import PostFilter
from .forms import PostForm


class NewsList(ListView):
    model = Post
    template_name = 'news_list.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-time_added')
    paginate_by = 10


class NewsSearchView(ListView):
    model = Post
    template_name = 'news_search.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-time_added')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class NewsDetailView(DetailView):
    model = Post
    template_name = 'news_contents.html'
    context_object_name = 'article'


class NewsCreateView(CreateView):
    template_name = 'news_create.html'
    form_class = PostForm


class NewsUpdateView(UpdateView):
    template_name = 'news_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class NewsDeleteView(DeleteView):
    template_name = 'news_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'










