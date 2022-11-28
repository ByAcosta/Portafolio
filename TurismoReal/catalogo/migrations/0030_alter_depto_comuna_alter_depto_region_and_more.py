# Generated by Django 4.1 on 2022-11-15 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0029_alter_inventario_id_depto_alter_inventario_id_i_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depto',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.comuna'),
        ),
        migrations.AlterField(
            model_name='depto',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.region'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='comuna',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.comuna'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.region'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.rol'),
        ),
    ]
