from django.db import models


class Sabores(models.Model):
    nome         = models.CharField(max_length=20, unique=True)
    ingredientes = models.CharField(max_length=300)

    def __str__(self):
        return self.nome


class Massa(models.Model):
    tipo = models.CharField(max_length=30, verbose_name="Tipo de Massa")

    def __str__(self):
        return self.tipo


class TamanhoPizza(models.Model):
    tamanho = models.CharField(max_length=30)

    def __str__(self):
        return self.tamanho


class PedirPizza(models.Model):
    id_sabor   = models.ForeignKey(Sabores, default=None, on_delete=models.CASCADE)
    id_tipo    = models.ForeignKey(Massa, default=None, on_delete=models.CASCADE)
    id_tamanho = models.ForeignKey(TamanhoPizza, default=None, on_delete=models.CASCADE)