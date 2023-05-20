# Create your models here.

from django.contrib.auth.models import User
from django.db import models

nivel_choices = [
    (1, 1),
    (3, 3),
    (5, 5),
    (8, 8),
]
prioridade_choices = [
    (1, 1),
    (2, 2),
    (3, 3),
]
situacao_choices = [
    ('Nova', 'Nova'),
    ('Em andamento', 'Em andamento'),
    ('Pendente', 'Pendente'),
    ('Resolvida', 'Resolvida'),
    ('Cancelada', 'Cancelada'),
]
#descricao
#responsavel
#nivel
#prioridade
#situacao

class Tarefa(models.Model):
    descricao = models.CharField(max_length=50)
    responsavel = models.CharField(blank=True, null=True)
    nivel = models.PositiveIntegerField(choices=nivel_choices)
    prioridade = models.PositiveIntegerField(choices=prioridade_choices)
    situacao = models.CharField(choices=situacao_choices)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    