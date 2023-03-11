from uuid import uuid4
from django.db import models
from apps.core.models import Contact
from apps.client.models import Client
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation



class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='users')
    contacts = GenericRelation(Contact)
