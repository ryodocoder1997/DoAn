from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'email', 'last_name', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=True)

        user.email = self.cleaned_data['email']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('account_type', 'is_agreed')