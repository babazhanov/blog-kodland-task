from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.list import ListView

from post.forms import PostForm
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 9


class PostDetailView(DetailView):
    model = Post


def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            post = Post()
            post.title = cleaned_data['title']
            post.content = cleaned_data['content']
            post.image = cleaned_data['image']
            post.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(request.FILES)

    return render(request, 'post/post_form.html', {'form': form})


