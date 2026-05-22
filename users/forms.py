from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import CustomUser


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=50, required=True)
    usable_password = None

    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password1', 'password2')
