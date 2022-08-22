# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
def print_resultado():
        alunos = input().split(' ')
        frequencia = input().split(' ')

        resultado = [
                    alunos[j]
                    for j in range(len(alunos)) if frequencia[j].count('A') or frequencia[j].count('P') >=1
                    if 100 - (frequencia[j].count('A') * 100) / (frequencia[j].count('P') + frequencia[j].count('A')) < 75
                     ]

        print(*resultado, sep=' ')

casos = int(input())
cont = 0
while True:
    cont += 1
    quant_alunos = int(input())
    print_resultado()
    if cont == casos:
        break
