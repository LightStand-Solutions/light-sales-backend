from .models import Client, Contact
from django.contrib import admin


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 0


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]

admin.site.register(Contact)
