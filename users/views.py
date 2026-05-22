from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('catalog:home')
