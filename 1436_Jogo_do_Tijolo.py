# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor = []
T = int(input())
for i in range(T):
    X = list(map(int, input().split()))
    jogadores_ordenados = sorted(X)
    x2 = int(len(jogadores_ordenados) / 2)
    for j in range(x2):
        if (X[0] % 2 != 0):
            case = X[x2]
            vetor.append(case)
            break
        else:
            case = X[x2+1]
            vetor.append(case)
            break
for i,j in enumerate(vetor):
    print('Case '+str(i+1)+': '+str(j))