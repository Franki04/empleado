# Generated by Django 4.2.1 on 2023-05-13 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departamento', '0002_alter_departamento_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='anulate',
            field=models.BooleanField(default=False, verbose_name='Anulado'),
        ),
        migrations.AlterField(
            model_name='departamento',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
    ]
