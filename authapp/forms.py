from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""
        # self.fields['username'].widget.attrs['placeholder'] = f'Логин'
        # self.fields['password'].widget.attrs['placeholder'] = f'Пароль'

        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control'


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password1'].label = ""
        self.fields['password2'].label = ""
        # self.fields['username'].widget.attrs['placeholder'] = f'Логин'
        # self.fields['password1'].widget.attrs['placeholder'] = f'Пароль'
        # self.fields['password2'].widget.attrs['placeholder'] = f'Повтор пароля '
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control'
            item.help_text = ''
