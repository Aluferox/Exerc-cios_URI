# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    num = input()
    if num[0] == '-':
        break
    elif num[:2] == '0x':
        print (int(num,0))
    else:
        aux1 = hex(int(num))
        aux2 = aux1[:2]
        aux3 = aux1[2:]
        print(aux2+aux3.upper())