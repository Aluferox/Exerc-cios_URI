# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
def fatorial(fat):
    resultado_fat = 1
    for i in range(fat,1,-1):
        resultado_fat = i * resultado_fat
    return resultado_fat

while(True):
    try:
        x1,x2 = map(int,input().split(" "))
        print(fatorial(x1) + fatorial(x2))
    except EOFError:
        break