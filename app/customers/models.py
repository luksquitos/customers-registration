from django.db import models

class Customer(models.Model):
    name = models.CharField("Nome", max_length=200)
    birth = models.DateField("Data de nascimento")
    cpf = models.CharField("CPF", max_length=14)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
