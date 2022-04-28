from django.db import models

# Create your models here.
class ferramenta(models.Model):
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    tipo = models.CharField(max_length=10)
    material = models.CharField(max_length=30)
    duracao = models.CharField(max_length=10)
    dataCadastro = models.CharField(max_length=10)
    funcao = models.CharField(max_length=30)

    def __str__(self):
        return self.codigo
