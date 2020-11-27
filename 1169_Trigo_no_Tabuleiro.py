# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor = []
N = int(input())
for i in range(N):
    graos = 1
    T = int(input())
    for j in range(T):
        graos *= 2

    vetor.append(graos)

for i in range(len(vetor)):
    print(int((vetor[i] / 12)/ 1000),'kg')