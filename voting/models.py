from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eleitor(models.Model):
    user = models.OneToOneField(User,related_name="eleitor",on_delete=models.CASCADE)

class Item(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=300)
    itens = models.ForeignKey(Eleitor,related_name="eleitor_item",on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.nome
class Vote(models.Model):
    eleitor_vote = models.OneToOneField(Eleitor,related_name="eleitor_vote",on_delete=models.CASCADE,null=True)
    item_vote = models.OneToOneField(Item,related_name="item_vote",on_delete=models.CASCADE,null=True)
