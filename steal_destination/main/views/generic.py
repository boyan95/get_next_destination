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
        context['first_six_destinations'] = self.object_list[:6]
        return context


