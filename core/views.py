from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse(f"<h1>Hello {nome} de {idade} anos</h1>")

def soma(request, parcela1, parcela2):
    return HttpResponse(f"<h1>O resultado da soma é: {parcela1 + parcela2}</h1>")

def multiplica(request, multiplicador, multiplicando):
    return HttpResponse(f"<h1>O resultado da multiplicação é: {multiplicador * multiplicando}</h1>")

def divide(request, dividendo, divisor):
    return HttpResponse(f"<h1>O resultado da divisão é: {dividendo / divisor}</h1>")

def subtrai(request, minuendo, subtraendo):
    return HttpResponse(f"<h1>O resultado da subtração é: {minuendo - subtraendo}</h1>")
