from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Introduzca el nombre de usuario',
        'class': 'text_field',
    }), label='Nombre usuario')
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Introduzca el correo',
        'class': 'text_field',
    }), label='Correo')

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Introduzca la contraseña',
        'class': 'text_field',
    }), label='Contraseña')

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita la sontraseña',
        'class': 'text_field',
    }), label='Verificar contraseña')


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Introduzca el nombre de usuario',
        'class': 'text_field',
    }), label='Nombre usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Introduzca la contraseña',
        'class': 'text_field',
    }), label='Contraseña')


class ChangePasswordForm(SetPasswordForm):
    new_password1_attrs = {
        'placeholder': 'Nueva contraseña',
        'class': 'form_field',
    }
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=new_password1_attrs), label='Contraseña nueva')
    new_password2_attrs = {
        'placeholder': 'Confirmar contraseña nueva',
        'class': 'form_field',
    }
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=new_password2_attrs), label='Contraseña nueva (confirmación)')


class ChangeOldPasswordForm(PasswordChangeForm):
    old_password_attrs = {
        'placeholder': 'Antigua contraseña',
        'class': 'form_field',
    }
    old_password = forms.CharField(widget=forms.PasswordInput(
        attrs=old_password_attrs), label='Contraseña antigua')
    new_password1_attrs = {
        'placeholder': 'Nueva contraseña',
        'class': 'form_field',
    }
    new_password1 = forms.CharField(widget=forms.PasswordInput(
        attrs=new_password1_attrs), label='Contraseña nueva')
    new_password2_attrs = {
        'placeholder': 'Confirmar contraseña nueva',
        'class': 'form_field',
    }
    new_password2 = forms.CharField(widget=forms.PasswordInput(
        attrs=new_password2_attrs), label='Contraseña nueva (confirmación)')


class EmailChangeForm(forms.Form):

    old_email = forms.EmailField(label='Antiguo correo')
    email1 = forms.EmailField(label='Nuevo correo', widget=forms.EmailInput)
    email2 = forms.EmailField(
        label='Nuevo correo (confirmación)', widget=forms.EmailInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EmailChangeForm, self).__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        email1 = cleaned_data['email1']
        email2 = cleaned_data['email2']
        old_email = cleaned_data['old_email']
        old_user_email = self.user.email

        if email1 != email2:
            self.add_error('email2', 'Los dos correos no coinciden')

        if old_user_email != old_email:
            self.add_error('old_email', 'Correo incorrecto')

    def save(self, commit=True):
        email = self.cleaned_data['email1']
        self.user.email = email
        if commit:
            self.user.save()
        return self.user


class EmailSubmitPasswordChange(forms.Form):
    email = forms.EmailField(label='Correo', widget=forms.EmailInput)


class VerificationCodePasswordChange(forms.Form):
    code = forms.IntegerField(label='Código', max_value=999999, min_value=100000)