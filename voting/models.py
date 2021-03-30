from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vote(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)

class Eleitor(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    vote = models.ForeignKey(Vote,related_name="user_vote",on_delete=models.CASCADE)
