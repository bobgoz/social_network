from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(
        template_name='social/index.html'), name='index'),
    path('meeting/', views.ProfileListView.as_view(), name='meeting'),
]