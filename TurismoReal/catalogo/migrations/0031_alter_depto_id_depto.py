# Generated by Django 4.1 on 2022-11-15 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0030_alter_depto_comuna_alter_depto_region_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depto',
            name='id_depto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
