# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
N = int(input())
x = list(map(int,input().split()))
vetor = [x for x in x]
menor = 0
posicao = 0

menor = vetor[0]
for i in range(len(vetor)):
    if(vetor[i] < menor):
        menor = vetor[i]
        posicao = i
print("Menor valor: %d" %menor)
print("Posicao: %d" %posicao)