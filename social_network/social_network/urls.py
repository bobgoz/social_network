from django.contrib import admin
from django.urls import path, include

from index import views

app_name = 'index'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', views.RegistrationUserView.as_view(), name='registration'),
    path('', include('index.urls'))
]
