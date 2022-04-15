from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views import generic as views

from steal_destination.main.models import Destination

UserModel = get_user_model()
user = UserModel


# RedirectToIndex
# @login_required()
class HomePageView(views.ListView):
    model = Destination
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.object_list:
            context['first_destination'] = self.object_list[0]
        # if self.object_list[1:6]:
        context['second_to__sixth_destinations'] = self.object_list[1:6]
        return context
