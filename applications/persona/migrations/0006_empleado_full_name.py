# Generated by Django 4.2.1 on 2023-05-14 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_hoja_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombres Completos'),
        ),
    ]
