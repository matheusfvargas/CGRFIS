from ast import Num
from pickle import TRUE
from pickletools import float8
import string
from subprocess import call
from warnings import catch_warnings
from django.db.models.fields import CharField
from django.forms import forms
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import ItemForm1, ItemForm2
import cgi, cgitb
import mammoth


# Create your views here.

import psycopg2   
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Cast

@login_required
def inicio(request):
    form1 = ItemForm1(request.POST or None)
    form2 = ItemForm2(request.POST or None)
    context = {
        'form1': form1,
        'form2': form2,
    }
    global xis
    global ipsilon
    if request.method == 'POST':
        xis = form1['ins_municipal1'].value()
        ipsilon = form2['ins_municipal2'].value()
        if xis.isdigit():
            return redirect('pvi:resposta')
        else: 
            return HttpResponse("Erro: dados incorretos")         
    else: 
        return render(request, 'item.html', context)
    
@login_required    
def resposta(request):
    global xis
    global ipsilon
    con = psycopg2.connect(host = '10.0.0.246', database='imobiliario', user='postgres', password='S3f1n*2022')
    con.autocommit = True
    with con.cursor() as curs:
        if int(ipsilon) == 0:
            aux = xis
            query1 = "select ins_municipal from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query2 = "select valor_met_evolutivo from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query3 = "select valor_met_regressao from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query4 = "select tipo_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query5 = "select nome_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux) 
            query6 = "select num_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query7 = "select parcelamento from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query8 = "select area_edificada from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query9 = "select uso_imovel from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query10 = "select area_terreno from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            curs.execute(query1) 
            inscricaox = curs.fetchone()[0]
            curs.execute(query2)
            valor_met_evolutivox = curs.fetchone()[0]
            curs.execute(query3)
            valor_met_regressaox = curs.fetchone()[0]
            curs.execute(query4)
            endereco1x= str(curs.fetchone()[0]) 
            curs.execute(query5)
            endereco2x = curs.fetchone()[0]
            curs.execute(query6)
            endereco3x = str(curs.fetchone()[0])
            curs.execute(query7)
            endereco4x = curs.fetchone()[0]
            enderecox = endereco1x + " "+ endereco2x + ", " + endereco3x + ", " + endereco4x
            curs.execute(query8)
            area_edificadax = curs.fetchone()[0]
            curs.execute(query9)
            uso_imovelx = curs.fetchone()[0]
            curs.execute(query10)
            area_terrenox = curs.fetchone()[0]
            context1 = {
            'inscricaox': inscricaox,
            'valor_met_evolutivox': valor_met_evolutivox, 
            'valor_met_regressaox': valor_met_regressaox,
            'enderecox': enderecox,
            'area_edificadax': area_edificadax,
            'area_terrenox': area_terrenox,
            'uso_imovelx': uso_imovelx}
            return render(request, 'detail1.html', context1)  
        else:
            aux = xis
            query1 = "select ins_municipal from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query2 = "select valor_met_evolutivo from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query3 = "select valor_met_regressao from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query4 = "select tipo_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query5 = "select nome_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux) 
            query6 = "select num_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query7 = "select parcelamento from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query8 = "select area_edificada from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query9 = "select uso_imovel from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query10 = "select area_terreno from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            curs.execute(query1) 
            inscricaox = curs.fetchone()[0]
            curs.execute(query2)
            valor_met_evolutivox = curs.fetchone()[0]
            curs.execute(query3)
            valor_met_regressaox = curs.fetchone()[0]
            curs.execute(query4)
            endereco1x= str(curs.fetchone()[0]) 
            curs.execute(query5)
            endereco2x = curs.fetchone()[0]
            curs.execute(query6)
            endereco3x = str(curs.fetchone()[0])
            curs.execute(query7)
            endereco4x = curs.fetchone()[0]
            enderecox = endereco1x + " "+ endereco2x + ", " + endereco3x + ", " + endereco4x
            curs.execute(query8)
            area_edificadax = curs.fetchone()[0]
            curs.execute(query9)
            uso_imovelx = curs.fetchone()[0]
            curs.execute(query10)
            area_terrenox = curs.fetchone()[0]
            aux = ipsilon
            query1 = "select ins_municipal from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query2 = "select valor_met_evolutivo from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query3 = "select valor_met_regressao from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query4 = "select tipo_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query5 = "select nome_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux) 
            query6 = "select num_endereco from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query7 = "select parcelamento from imobiliario.public.itbi where ins_municipal LIKE '%s';" % str(aux)
            query8 = "select area_edificada from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query9 = "select uso_imovel from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            query10 = "select area_terreno from imobiliario.public.itbi where ins_municipal LIKE '%s'" %str(aux)
            curs.execute(query1) 
            inscricaoy = curs.fetchone()[0]
            curs.execute(query2)
            valor_met_evolutivoy = curs.fetchone()[0]
            curs.execute(query3)
            valor_met_regressaoy = curs.fetchone()[0]
            curs.execute(query4)
            endereco1y= str(curs.fetchone()[0]) 
            curs.execute(query5)
            endereco2y = curs.fetchone()[0]
            curs.execute(query6)
            endereco3y = str(curs.fetchone()[0])
            curs.execute(query7)
            endereco4y = curs.fetchone()[0]
            enderecoy = endereco1y + " "+ endereco2y + ", " + endereco3y + ", " + endereco4y
            curs.execute(query8)
            area_edificaday = curs.fetchone()[0]
            curs.execute(query9)
            uso_imovely = curs.fetchone()[0]
            curs.execute(query10)
            area_terrenoy = curs.fetchone()[0]
            context2 = {
            'inscricaox': inscricaox,
            'valor_met_evolutivox': valor_met_evolutivox, 
            'valor_met_regressaox': valor_met_regressaox,
            'enderecox': enderecox,
            'area_edificadax': area_edificadax,
            'area_terrenox': area_terrenox,
            'uso_imovelx': uso_imovely,
            'area_edificaday': area_edificaday,
            'area_terrenoy': area_terrenoy,
            'uso_imovely': uso_imovely,
            'inscricaoy': inscricaoy,
            'valor_met_evolutivoy': valor_met_evolutivoy, 
            'valor_met_regressaoy': valor_met_regressaoy,
            'enderecoy': enderecoy}
            return render(request, 'detail2.html', context2)

def observatorio(request):
    return HttpResponse("Em execução")

@login_required
def excel(request):
    return HttpResponse("Em execução")   


