from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = UsernameField(
        initial="admin.user",
        widget=forms.TextInput(attrs={
            "class": "form-control"})
    )
    password = forms.CharField(
        initial="1qazcde3",
        widget=forms.PasswordInput(attrs={
            "class": "form-control"})
    )
