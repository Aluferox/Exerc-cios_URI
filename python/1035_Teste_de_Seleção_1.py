# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
A,B,C,D = map(int,input().split(" "))
if B > C and D > A and C > 0 and D > 0 and C + D > A + B and (A % 2) == 0:
    print("Valores aceitos")
else:
    print("Valores nao aceitos")