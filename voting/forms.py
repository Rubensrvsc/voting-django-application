from django import forms

class UserSignUpForm(forms.Form):
    
    username = forms.CharField(label="Usuário")
    password1 = forms.CharField(label="Senha", widget = forms.PasswordInput)
    password2 = forms.CharField(label="Confirme", widget = forms.PasswordInput)