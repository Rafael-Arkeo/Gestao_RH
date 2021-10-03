# Generated by Django 3.2.7 on 2021-10-03 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0007_alter_funcionario_empresa'),
        ('documentos', '0003_alter_documento_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='funcionario',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.PROTECT, to='funcionarios.funcionario'),
        ),
    ]
