from django.contrib.auth.forms import UserCreationForm, UserChangeForm, \
    AuthenticationForm
# from django.forms import forms
from django import forms
# from django.contrib.auth.forms import

from authapp.models import TravelUser, TravelUserProfile


class TravelUserRegisterForm(UserCreationForm):
    '''Форма регистрации в проекте'''
    class Meta:
        model = TravelUser
        fields = (
            'username', 'first_name', 'password1',
            'password2', 'email', 'age', 'avatar'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("Вы слишком молоды!")

        return data


class TravelUserEditForm(UserChangeForm):
    '''Редактирование стандартного профиля user'''
    class Meta:
        model = TravelUser
        fields = ('username', 'first_name', 'email', 'age', 'avatar',
                  'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()

    def clean_age(self):
        data = self.cleaned_data['age']
        if data < 18:
            raise forms.ValidationError("ВЫ слишком молоды!")

        return data


class TravelUserLoginForm(AuthenticationForm):
    '''Форма аутентификации'''
    class Meta:
        model = TravelUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(TravelUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TravelUserProfileEditForm(forms.ModelForm):
    '''Форма редактирования расширенного профиля'''
    class Meta:
        model = TravelUserProfile
        fields = ('tagline', 'aboutMe', 'gender')

    def __init__(self, *args, **kwargs):
        super(TravelUserProfileEditForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
