# Generated by Django 5.1 on 2024-09-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0005_alter_group_invest_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipo_articulo',
            name='tipo',
            field=models.CharField(choices=[('default_value', 'Default Value'), ('informe_tecnico', 'Informe Técnico'), ('acta_congreso', 'Acta de Congreso'), ('revista_cientifica', 'Revista Científica')], default='default_value', max_length=100),
        ),
    ]
