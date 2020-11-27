# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
resultado = 0
cont =0
caw_caw = 'caw caw'
vetor = []

for i in range(3):
    olho = ''
    while (olho != caw_caw):
        olho = input()
        if olho == '0':
            break
        if (olho != caw_caw):
            if (olho == '--*'):
                resultado += 1
            elif (olho == '-*-'):
                resultado += 2
            elif (olho == '-**'):
                resultado += 3
            elif (olho == '*--'):
                resultado += 4
            elif (olho == '*-*'):
                resultado += 5
            elif (olho == '**-'):
                resultado += 6
            elif (olho == '***'):
                resultado += 7

    print(resultado)
    resultado = 0








