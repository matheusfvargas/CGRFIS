# Generated by Django 4.0.4 on 2022-05-10 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditor', models.CharField(max_length=80)),
                ('matricula', models.IntegerField()),
                ('data_relatorio', models.DateField(auto_now=True)),
                ('os', models.IntegerField()),
                ('ano', models.IntegerField()),
                ('processo_adm', models.IntegerField()),
                ('objeto_processo', models.CharField(max_length=300)),
                ('objeto_os', models.CharField(max_length=300)),
                ('cnpj', models.CharField(max_length=80)),
                ('nome_contrib', models.CharField(max_length=80)),
                ('ins_imobiliaria', models.BigIntegerField()),
                ('nlct', models.IntegerField()),
                ('guia_dam', models.IntegerField()),
                ('valor_avaliacao', models.DecimalField(decimal_places=2, max_digits=18)),
                ('valor_itbi', models.DecimalField(decimal_places=2, max_digits=18)),
                ('data_lancamento', models.DateField()),
                ('data_vencimento', models.DateField()),
                ('data_pagamento', models.DateField()),
                ('status_pagamento', models.CharField(max_length=80)),
                ('periodo_ini', models.DateField()),
                ('periodo_fim', models.DateField()),
                ('obs', models.CharField(max_length=300)),
            ],
        ),
    ]