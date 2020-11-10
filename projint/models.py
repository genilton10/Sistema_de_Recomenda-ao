
from django.db import models
from django.utils import timezone

class Classe(models.Model):

    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    detalhe = models.TextField()

    def __str__(self):

        return self.nome