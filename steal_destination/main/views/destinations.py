from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views import generic as views

from steal_destination.main.forms import CreateDestinationForm, EditDestinationForm
from steal_destination.main.models import Destination


class CreateDestinationView(LoginRequiredMixin, views.CreateView):
    model = Destination
    form_class = CreateDestinationForm
    template_name = 'main/destination_create.html'
    success_url = reverse_lazy('destinations')
    raise_exception = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class DestinationsView(LoginRequiredMixin, views.ListView):
    model = Destination
    template_name = 'main/destinations.html'
    context_object_name = 'destinations'
    paginate_by = 6
    raise_exception = True

    def get_queryset(self):
        return super().get_queryset().order_by('country_name')


class DestinationDetailsView(LoginRequiredMixin, views.DetailView):
    model = Destination
    template_name = 'main/destination_details.html'
    context_object_name = 'destination'
    raise_exception = True

    # form_class = CommentForm
    # second_form_class = ReplyForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(Destination, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        # context['comment_owner'] = self.request.comments.user_id == self.object.user
        context['is_owner'] = self.object.user == self.request.user
        context['total_likes'] = total_likes
        return context


def likes_destination(request, pk):
    post = get_object_or_404(Destination, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('destination', args=[str(pk)]))
    # destination = Destination.objects.get(pk=pk)
    # if destination.likes == 0:
    #     destination.likes += 1
    #     destination.save()
    # return redirect('destination', pk)


class EditDestinationView(LoginRequiredMixin, views.UpdateView):
    model = Destination
    form_class = EditDestinationForm
    template_name = 'main/destination_edit.html'
    raise_exception = True
    def get_success_url(self):
        return reverse_lazy('destination', kwargs={'pk': self.object.id})


class DeleteDestinationView(LoginRequiredMixin, views.DeleteView):
    model = Destination
    template_name = 'main/destination_delete.html'
    success_url = reverse_lazy('destinations')
    raise_exception = True
