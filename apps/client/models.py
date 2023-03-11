from django.db import models
from ..core.enums import Name
from ..core.models import Core, Contact
from django.contrib.contenttypes.fields import GenericRelation


class Client(Core):
    name = models.CharField(max_length=Name.MAX_LENGTH.value)
    cnpj = models.CharField(max_length=20)
    contacts = GenericRelation(Contact)

    def __str__(self):
        return self.name