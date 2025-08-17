from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """Кастомная форма, унаследованная от UserCreationForm"""

    first_name = forms.CharField(
        label='Имя',
        required=True,
        )

    last_name = forms.CharField(
        label='Фамилия',
        required=True,
        )
    
    phone = forms.IntegerField(
        label='Номер телефона',
        required=True,

    )
    
    email = forms.EmailField(
        label='Почта',
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name',
                                                 'last_name',
                                                 'phone',
                                                 'email',
                                                 )
