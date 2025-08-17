from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.views.generic import (
    CreateView,
    ListView,
)

User = get_user_model()


class RegistrationUserView(CreateView):
    """Вью для регистрации."""

    template_name = r'registration\registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')


class ProfileListView(ListView):
    """Вью для отображения списка профилей"""

    model = User
    template_name = 'social/meeting.html'
    context_object_name = 'profile'
