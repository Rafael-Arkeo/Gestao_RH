# Generated by Django 3.2.7 on 2021-10-03 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0001_initial'),
        ('funcionarios', '0008_alter_funcionario_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.PROTECT, to='empresas.empresa'),
        ),
    ]
