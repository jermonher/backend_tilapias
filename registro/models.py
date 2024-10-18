from django.db import models

class Monitoreo(models.Model):
    ph = models.DecimalField(max_digits=4, decimal_places=2)
    oxigeno = models.DecimalField(max_digits=4, decimal_places=2)
    temperatura = models.DecimalField(max_digits=4, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Monitoreo {self.id} - {self.fecha}"

class ApiKey(models.Model):
    key = models.CharField(max_length=40, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.key