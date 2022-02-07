from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    # first_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    # last_name = forms.CharField(max_length=50, required=False, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
    class Meta :
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'placeholder': 'Username'})}

class MyAuthenticationForm(AuthenticationForm) :
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'validate','placeholder': 'Enter Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password'}))

class GroupForm(forms.Form) :
    group = forms.CharField(label='', max_length=255,widget=forms.PasswordInput(attrs={'placeholder':'Enter Room Name to Create', 'class':'inpt-fld'}))

class JoinForm(forms.Form) :
    room_id = forms.CharField(label='', max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'Enter Room Code to Join', 'class':'inpt-fld'}))