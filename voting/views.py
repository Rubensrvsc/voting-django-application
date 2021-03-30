from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.

class SignUpView(generic.View):

    template_name = 'signup.html'

    def get(self,request):
        data = { 'form': UserSignUpForm()}
        return render(request,self.template_name,data)
    
    def post(self,request):
        form = UserSignUpForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')

            if username and password1 and password2 and password1 == password2:
                user = User.objects.create_user(
                    username=username,
                    password=password1
                )
                Eleitor.objects.create(user=user)

                if user:
                    return render(request,"index.html")
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }
        return render(request, self.template_name, data)