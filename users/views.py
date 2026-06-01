from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config import settings
from users.forms import UserRegisterForm
from users.models import CustomUser


class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'users/user_form.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать!'
        message = 'Спасибо, что зарегистрировались! Теперь Вам доступны действия на сайте'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)
