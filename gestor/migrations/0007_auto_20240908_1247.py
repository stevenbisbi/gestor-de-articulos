# Generated by Django 5.1 on 2024-09-08 17:47

from django.db import migrations
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin1234'
        )

class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0006_alter_tipo_articulo_tipo'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
