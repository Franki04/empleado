# Generated by Django 4.2.1 on 2023-05-26 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0006_empleado_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
