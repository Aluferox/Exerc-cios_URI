# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    tecla_apagada,contrato = (input().split())
    if tecla_apagada == '0' and contrato == '0':
        break
    new_string = contrato.replace(tecla_apagada,"")
    aux = new_string.lstrip('0')
    if aux == '' and tecla_apagada != '0' and contrato != '0':
        print('0')
    else:
        print(aux)