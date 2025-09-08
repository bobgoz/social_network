from django.urls import path
from django.views.generic import TemplateView

from . import views


urlpatterns = [
    path('', TemplateView.as_view(
        template_name='social/index.html'), name='index'),
    path('meeting/', views.ProfileListView.as_view(), name='meeting'),
    path('profile/<slug:username>/', views.ProfileDetailView.as_view(), name='profile_detail'),
    path('forum/', TemplateView.as_view(template_name='social/forum.html'), name='forum'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('resources/', TemplateView.as_view(template_name='social/resources.html'), name='resources'),
]