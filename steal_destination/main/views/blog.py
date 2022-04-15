from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from steal_destination.main.forms import BlogForm, EditArticleForm
from steal_destination.main.models import Blog, Destination


class CreateArticleView(views.CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'main/article_create.html'
    success_url = reverse_lazy('blog')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class BlogView(views.ListView):
    model = Blog
    template_name = 'main/blog.html'
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        return super().get_queryset().order_by('article_name')


class ArticleDetailsView(views.DetailView):
    model = Blog
    template_name = 'main/article_details.html'
    context_object_name = 'current_article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Blog, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['is_owner'] = self.object.user == self.request.user
        context['total_likes'] = total_likes
        return context


def likes_article(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article details', args=[str(pk)]))




class EditArticleView(views.UpdateView):
    model = Blog
    form_class = EditArticleForm
    template_name = 'main/article_edit.html'
    context_object_name = 'article'

    def get_success_url(self):
        return reverse_lazy('destination', kwargs={'pk': self.object.id})


class DeleteDestinationView(views.DeleteView):
    model = Blog
    template_name = 'main/article_delete.html'
    success_url = reverse_lazy('destinations')
