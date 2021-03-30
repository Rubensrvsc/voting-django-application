from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
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

class LoginView(generic.View):

    template_name = "login.html"

    def get(self,request):
        data = {"form": UserLoginForm()}

        return render(request,self.template_name,data)
    
    def post(self,request):
        form = UserLoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
           
            if username and password and user is not None:
                
                login(request, user)
                return redirect('index')
        
        data = { 
            'form': form,
            'error': 'Usuário ou senha inválidos'
        }     
        return render(request, self.template_name, data)

class IndexView(LoginRequiredMixin,generic.View):

    template_name = "index.html"

    @method_decorator(login_required)
    def get(self,request):
        data = {"user": request.user}
        return render(request,self.template_name,data)

class LogoutView(generic.View):

    @method_decorator(login_required)
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))