from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    """
    Form for registering a new user.

    Inherits:
    - UserCreationForm: Provides fields for username, password1, and password2.

    Additional Field:
    - email (EmailField): Field for user's email.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    """
    Form for updating user information.

    Inherits:
    - ModelForm: Automatically creates form fields based on the User model.

    Fields:
    - email (EmailField): Field for user's email.
    """

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    """
    Form for updating user profile information.

    Inherits:
    - ModelForm: Automatically creates form fields based on the Profile model.

    Fields:
    - image (ModelField): Field for updating the profile image.
    """
    
    class Meta:
        model = Profile
        fields = ['image']