from django.db import models
from ..core.enums import Name
from ..core.models import Core


class Client(Core):
    name = models.CharField(max_length=Name.MAX_LENGTH.value)
    cnpj = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Contact(Core):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='contacts')

    def __str__(self):
        return f'{self.name} ({self.client.name})'

    class Meta:
        ordering = ['-created_at']
