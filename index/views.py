from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)

from .forms import (
    CustomUserCreationForm,
    NewsCreationForm,
    )
from .models import News

User = get_user_model()


class RegistrationUserView(CreateView):
    """Вью для регистрации."""

    template_name = 'registration\registration.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')


class ProfileListView(ListView):
    """Вью для отображения списка профилей"""

    model = User
    template_name = 'social/meeting.html'


class ProfileDetailView(DetailView):
    """Вью для детального отображения профиля"""

    model = User
    template_name = 'social/profile.html'
    slug_url_kwarg = 'username'
    context_object_name = 'profile'
    slug_field = 'username'
    
    
class NewsListView(ListView):
    """Вью для отображения списка новостей"""
    model = News
    template_name = 'social/news.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['news_form'] = NewsCreationForm
        return context
