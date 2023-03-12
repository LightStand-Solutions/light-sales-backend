from .models import Client, Contact
from django.contrib import admin
from ..user.models import User


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 0


class UserInLine(admin.TabularInline):
    model = User
    extra = 0
    max_num = 0
    fields = [
        'email',
        'first_name',
        'last_name'
    ]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [ContactInLine, UserInLine]


admin.site.register(Contact)
