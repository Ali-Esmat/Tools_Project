from django import forms
from django.contrib.auth.forms import UserCreationForm
from models import Users

class SignupForm(UserCreationForm):
    user_name = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(max_length=200, required=True)
    user_type = forms.forms.CharField(max_length= 200, required=True)
    class Meta:
        model = Users
        fields = ('user_name', 'password', 'user_type')