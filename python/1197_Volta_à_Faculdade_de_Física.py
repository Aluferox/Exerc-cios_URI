# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor = []
while(True):
    try:
        x1,x2 = map(int,input().split(" "))
        deslocamento = (x1 * x2) * 2
        vetor.append(deslocamento)
        print(deslocamento)
    except:
        break