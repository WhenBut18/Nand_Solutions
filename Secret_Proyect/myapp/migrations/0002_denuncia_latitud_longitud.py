# Generated by Django 4.2.4 on 2023-10-23 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='denuncia',
            name='Latitud_Longitud',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]