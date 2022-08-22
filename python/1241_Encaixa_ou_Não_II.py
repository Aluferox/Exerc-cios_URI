# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
casos = int(input())
for i in range(casos):
    A,B = input().split(' ')
    tamanho_B = len(B)
    if B in A[-tamanho_B:]:
        print('encaixa')
    else:
        print('nao encaixa')
