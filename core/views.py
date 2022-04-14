from django.shortcuts import render, HttpResponse

# Create your views here.

def soma(request, num1=0, num2=0):
    Soma = num1 + num2
    return HttpResponse(f'A soma ficou {Soma}')

def vezes(request, num1=0, num2=0):
    VEZES = num1 * num2
    return HttpResponse(f'Vezes deu: {VEZES}')

def dividir(request, num1=0, num2=0):
    DIVIDIR = num1 / num2
    return HttpResponse(f'A conta de dividir foi: {DIVIDIR}')

def menos(request, num1=0, num2=0):
    MENOS = num1 - num2
    return HttpResponse(f'Conta de menos foi {MENOS}')