# Generated by Django 3.2.8 on 2021-11-02 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_auto_20211102_0859'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='fecha',
            field=models.DateField(blank=True, help_text='Fecha de publicación', null=True),
        ),
    ]