from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
import psycopg2
from .models import Dados
from .forms import formulario_processo, lista_processo, edita_processo
from django.db import connection, transaction


# Create your views here.

def index(request):
    context ={

    }
    return render(request, 'index.html', context)
'''
def consulta_processo(request):
   conn = psycopg2.connect("dbname=stage_sefin user=postgres")
   cur = conn.cursor()
   cur.execute("SELECT * FROM stage_sefin.public.relatorio_dados") 
   records = cur.fetchall()
def consulta_assunto(request):
    conn = psycopg2.connect("dbname=stage_sefin user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stage_sefin.public.relatorio_dados") 
    records = cur.fetchall()
def consulta_auditor(request):
    conn = psycopg2.connect("dbname=stage_sefin user=postgres")
    cur = conn.cursor()
    cur.execute("SELECT * FROM stage_sefin.public.relatorio_dados") 
    records = cur.fetchall()
'''
def incluir_processo(request):
    conn = psycopg2.connect(host = '10.0.0.246', database='imobiliario', user='postgres', password='S3f1n*2022')
    cur = conn.cursor()
    form = formulario_processo(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('itbi:index')
    return render(request, 'incluir_processo.html',{'form':form})

def listar_processo(request):
    global processo, ano
    form2 = lista_processo(request.POST or None)
    if form2.is_valid():
        processo = form2.cleaned_data['processo_adm']
        ano = form2.cleaned_data['ano']
        return redirect ('itbi:editar_processo') 
    return render (request, 'listar_processo.html', {'form2':form2})
        
        
def editar_processo(request):
    global processo, ano
    conn = psycopg2.connect(host = '10.0.0.246', database='imobiliario', user='postgres', password='S3f1n*2022')
    cur = conn.cursor()
    conn.autocommit = True
    cur.execute("SELECT auditor, matricula,objeto_processo, cnpj, nome_contrib, ins_imobiliaria from stage_sefin.public.relatorio_dados where processo_adm =(%s) and ano = (%s)", (processo, ano))
    aux = cur.fetchall()[0]
    auditor = aux[0]
    matricula = aux[1]
    objeto = aux[2]
    cnpj = aux[3]
    nome_contrib = aux[4]
    ins_imobiliaria = aux[5]
    
    form3 = edita_processo(request.POST)
        
    context ={
    'processo':processo,
    'ano': ano,
    'auditor': auditor,
    'matricula': matricula,
    'objeto': objeto,
    'cnpj': cnpj,
    'nome_contrib': nome_contrib,
    'ins_imobiliaria': ins_imobiliaria,
    'form3':form3,
        }   
    if form3.is_valid():
        
        auditor = form3.cleaned_data['auditor']
        matricula = form3.cleaned_data['matricula']
        objeto = form3.cleaned_data['objeto_processo']
        cnpj = form3.cleaned_data['cnpj']
        nome_contrib = form3.cleaned_data['nome_contrib']
        ins_imobiliaria = form3.cleaned_data['ins_imobiliaria']
        cur.execute("UPDATE stage_sefin.public.relatorio_dados SET auditor =(%s), matricula =(%s), objeto = (%s), cnpj =(%s), nome_contrib =(%s), ins_imobiliaria =(%s) where processo_adm =(%s) and ano = (%s)", (auditor, matricula, objeto, cnpj, nome_contrib, ins_imobiliaria, processo, ano))
        return redirect ('itbi:index')
    return render (request, 'editar_processo.html', context)

