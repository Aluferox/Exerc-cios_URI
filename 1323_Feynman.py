# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import pow
feynman = -1
vetor = []

while(feynman != 0):
    soma = 0
    feynman = int(input())
    if(feynman != 0):
        for i in range(feynman,0,-1):
            soma+= int(pow(i,2))

        vetor.append(soma)
for i in vetor:
    print(i)