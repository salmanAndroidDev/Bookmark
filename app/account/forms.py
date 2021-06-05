from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class LoginForm(forms.Form):
    """Simple Form to login"""
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    """Simple Form for user registration"""
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """password2 should be the same as password"""
        cd = self.cleaned_data
        if cd['password2'] != cd['password']:
            raise forms.ValidationError("2 passwords are not the same")
        return cd['password2']


class UserEditForm(forms.ModelForm):
    """Form class to modify User"""

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    """Form class to modify Profile"""
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')