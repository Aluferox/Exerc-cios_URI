# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

casos = int(input())

for i in range(casos):
    entrada = input().lower()
    x = list({i for i in entrada if i.isalpha()})
    freq = [entrada.count(i) for i in x]

    maior = max(freq)

    saida = ''

    for i in range(len(freq)):
        if freq[i] >= maior:
            saida += x[i]
    print(''.join(sorted(saida)))