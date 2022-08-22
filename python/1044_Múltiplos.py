# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
a,b = (input(). split())
a = int(a)
b = int(b)
maior = max(a,b)
menor = min(a,b)
if maior % menor == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')