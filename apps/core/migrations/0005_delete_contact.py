# Generated by Django 4.1.7 on 2023-03-12 00:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_contact_object_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
