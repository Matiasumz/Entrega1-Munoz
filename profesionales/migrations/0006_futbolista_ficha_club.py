# Generated by Django 4.0.3 on 2022-05-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profesionales', '0005_cerrajero_fecha_creacion_futbolista_fecha_creacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='futbolista',
            name='ficha_club',
            field=models.ImageField(blank=True, null=True, upload_to='ficha'),
        ),
    ]
