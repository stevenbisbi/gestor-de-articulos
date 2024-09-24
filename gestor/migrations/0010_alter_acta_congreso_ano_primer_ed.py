from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0009_alter_acta_congreso_ano_primer_ed'),  
    ]

    operations = [
        migrations.AddField(
            model_name='acta_congreso',
            name='ano_primer_ed',
            field=models.IntegerField(null=True, blank=True),  # Permite valores nulos si es necesario
        ),
    ]
