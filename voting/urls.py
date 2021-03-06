from django.contrib import admin
from django.urls import path,include
from .views import *
urlpatterns = [
    
    path('',SignUpView.as_view(),name="signup"),
    path('login',LoginView.as_view(),name="login"),
    path('index',IndexView.as_view(),name="index"),
    path('logout',LogoutView.as_view(),name="logout"),
    path('cadastrar',CadastrarItemView.as_view(),name="cadastrar_item"),
    path('voto/<int:id>/<str:username>',VotoItemView.as_view(),name="voto"),
    path('votos/<int:id_voto>',VerVotosView.as_view(),name="votos_item"),
    path('ver_seus_votos',VerSeusVotosView.as_view(),name="ver_seus_votos")

]
