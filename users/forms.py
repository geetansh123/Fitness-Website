from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

from users.models import NewUser

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    
    class Meta:
        model=NewUser
        fields=('email','user_name','first_name','age','gender','blood_group','height','weight','goal','password1','password2')

class LoginForm(forms.ModelForm):
    password=forms.CharField(label="Password",widget=forms.PasswordInput)
    
    class Meta:
        model=NewUser
        fields=('email','password')

    def clean(self):
    	email=self.cleaned_data['email']
    	password=self.cleaned_data['password']
    	if not authenticate(email=email,password=password):
    		raise forms.ValidationError("Invalid Login")
