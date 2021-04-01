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
from django.db.models import Q
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

                auth = authenticate(request,username=username, password=password1)
           
                if username and password1 and auth is not None:
                
                    login(request, auth)
                    return redirect('index')
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
        data = {"user": request.user,
        "itens": Item.objects.filter(~Q(itens__user__username=request.user.username) & ~Q(item_vote__eleitor_vote__user__username=request.user.username))}
        return render(request,self.template_name,data)

class LogoutView(generic.View):

    @method_decorator(login_required)
    def get(self,request):
        logout(request)
        return HttpResponseRedirect(reverse('login'))

class CadastrarItemView(generic.CreateView):

    template_name = "cadastrar_item.html"

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = ItemForm()
        return render(request,self.template_name,{'form':form})
    
    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST)
        print(request.user.eleitor)
        if form.is_valid():
            item = form.save(commit=False)

            item.itens = request.user.eleitor
            item.save()
            return redirect('index')
        return render(request,self.template_name,{'form':form})
    
class VotoItemView(generic.View):


    @method_decorator(login_required)
    def get(self,request,id: int,username):

        eleitor = Eleitor.objects.get(user__username=username)
        item = Item.objects.get(id=id)
        Vote.objects.create(
            eleitor_vote=eleitor,
            item_vote=item
        )
        return redirect('index')

    @method_decorator(login_required)
    def post(self, request, *args, **kwargs):
        return redirect('index')

class VerVotosView(generic.View):

    template_name = "votos_item.html"

    @method_decorator(login_required)
    def get(self, request, id_voto: int):
        data = {'user':request.user,
            'votos': Vote.objects.filter(item_vote__id=id_voto)
        }
        return render(request,self.template_name,data)
    

    