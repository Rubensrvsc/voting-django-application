from django import forms
from .models import *

class UserSignUpForm(forms.Form):
    
    username = forms.CharField(label="Usuário")
    password1 = forms.CharField(label="Senha", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Confirme", widget = forms.PasswordInput)

class UserLoginForm(forms.Form):

    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget = forms.PasswordInput)

class ItemForm(forms.ModelForm):

    class Meta:
        model = Item
        fields = ['nome','descricao']