from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from steal_destination.main.forms import CommentForm
from steal_destination.main.models import Comments
from django.views import generic as views


class CreateCommentView(LoginRequiredMixin, views.CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'main/add_comment.html'
    raise_exception = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.destination_id = self.kwargs['pk']
        form.instance.user_id = self.request.user.pk
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('destination', kwargs={'pk': self.object.destination_id})

# class EditCommentView(views.UpdateView):
#     model = Comments
#     form_class = EditCommentForm
#     template_name = 'main/edit_comment.html'
#
#     def get_success_url(self):
#         return reverse_lazy('destination', kwargs={'pk': self.object.destination_id})
#
#
# class DeleteCommentsView(views.DeleteView):
#     model = Comments
#     template_name = 'main/delete_comment.html'
#
#     def get_success_url(self):
#         return reverse_lazy('destination', kwargs={'pk': self.object.destination_id})
