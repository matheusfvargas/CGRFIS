from django.db import models

# Create your models here.

class Dados(models.Model):

    auditor = models.CharField(max_length = 80)
    matricula = models.IntegerField()
    data_relatorio = models.DateField(auto_now = True)
    os = models.IntegerField()
    ano = models.IntegerField()
    processo_adm = models.IntegerField()
    objeto_processo = models.CharField(max_length = 300)
    objeto_os = models.CharField(max_length = 300)
    cnpj = models.CharField(max_length=80)
    nome_contrib = models.CharField(max_length=80)
    ins_imobiliaria = models.BigIntegerField()
    nlct = models.IntegerField()
    guia_dam = models.IntegerField()
    valor_avaliacao = models.DecimalField(max_digits=18 ,decimal_places=2)
    valor_itbi = models.DecimalField(max_digits =18, decimal_places=2)
    data_lancamento = models.DateField()
    data_vencimento = models.DateField()
    data_pagamento = models.DateField()
    status_pagamento = models.CharField(max_length=80)
    periodo_ini = models.DateField()
    periodo_fim = models.DateField()
    obs = models.CharField(max_length = 300)