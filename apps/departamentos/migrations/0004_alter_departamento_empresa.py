# Generated by Django 3.2.7 on 2022-05-31 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('departamentos', '0003_alter_departamento_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
