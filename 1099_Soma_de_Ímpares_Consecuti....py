# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
N = int(input())
vetor = []
for i in range(N):
    X = list(map(int,input().split(" ")))
    A1 = min(X)
    A2 = max(X)
    if(A1 < A2):
        vetor.append([A1,A2])
    else:
        vetor.append([A1,A2])
for n in vetor:
    soma = 0
    for i in range(n[0] + 1, n[1]):
        if (i % 2 != 0):
            soma += i
    print(soma)