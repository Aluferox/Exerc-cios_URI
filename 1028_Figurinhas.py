# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
tentativas = int(input())
for i in range(tentativas):
    MDC_1, MDC_2 = map(int, input().split())
    maior = max(MDC_1, MDC_2)
    menor = min(MDC_1,MDC_2)

    if maior % menor == 0:
        print(menor)
        continue
    resto = menor
    while True:
        # resto = maior % menor

        if maior % resto == 0:
            print(resto)
            break
        menor = maior % resto
        maior = resto
        resto = menor