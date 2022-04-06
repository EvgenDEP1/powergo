from django import forms

from mainapp.models import Mail


class MailForm(forms.ModelForm):
    class Meta:
        model = Mail
        fields = (
            'name',
            'email',
            'text',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = f'Имя'
        self.fields['email'].widget.attrs['placeholder'] = f'Почта'
        self.fields['text'].widget.attrs['placeholder'] = f'Сообщение...'
        for name, item in self.fields.items():
            item.widget.attrs['class'] = f'form-control'
            item.help_text = ''
