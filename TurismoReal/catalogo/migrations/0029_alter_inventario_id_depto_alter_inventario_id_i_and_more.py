# Generated by Django 4.1 on 2022-11-15 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0028_alter_usuario_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='id_depto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.depto'),
        ),
        migrations.AlterField(
            model_name='inventario',
            name='id_i',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
