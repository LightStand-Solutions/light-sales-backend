# Generated by Django 4.1.7 on 2023-03-11 04:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=225)),
                ('cnpj', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]