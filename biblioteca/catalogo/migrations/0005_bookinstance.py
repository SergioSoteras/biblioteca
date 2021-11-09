# Generated by Django 3.2.8 on 2021-11-03 09:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0004_auto_20211103_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('due_back', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('m', 'Mantenimiento'), ('o', 'En préstamo'), ('a', 'Disponible'), ('r', 'Reservado')], default='m', help_text='Disponibilidad', max_length=1)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalogo.book')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
    ]