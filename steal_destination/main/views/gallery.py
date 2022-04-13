from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render, get_object_or_404


from steal_destination.main.models import Post, PostImage


def blog_view(request):
    posts = Post.objects.all()
    return render(request, 'main/gallery.html', {'posts': posts})


def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    photos = PostImage.objects.filter(post=post)
    return render(request, 'main/gallery_detail.html', {
        'post': post,
        'photos': photos
    })


