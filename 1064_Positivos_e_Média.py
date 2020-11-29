# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
cont = 0
media = 0
for i in range(6):
    N = float(input())
    if(N > 0):
        cont += 1
        media +=  N
print(str(cont)+" valores positivos")
print("{:.1f}".format(media / cont))