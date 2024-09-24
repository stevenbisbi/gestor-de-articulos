from django.db import migrations, models


def set_year_for_existing_records(apps, schema_editor):
    # Obtener el modelo `Acta_congreso`
    ActaCongreso = apps.get_model('gestor', 'Acta_congreso')
    for acta in ActaCongreso.objects.all():
        # Asignar el año de la fecha `ano_primer_ed` al nuevo campo
        acta.ano_primer_ed = acta.ano_primer_ed.year
        acta.save()


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0008_alter_tipo_articulo_tipo'),
    ]

    operations = [
        # Primero, convierte las fechas a años
        migrations.RunPython(set_year_for_existing_records),
        # Luego, cambia el tipo de campo a IntegerField
        migrations.AlterField(
            model_name='acta_congreso',
            name='ano_primer_ed',
            field=models.IntegerField(),
        ),
    ]
