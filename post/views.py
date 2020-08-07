from django.shortcuts import render
from django.views.generic import DetailView, CreateView
from django.views.generic.list import ListView
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'image']
