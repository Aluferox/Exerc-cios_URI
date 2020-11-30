# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
L = int(input())
T = input()
vetor = []
soma = 0
cont = 0
for i in range(12):
    linha = []
    for j in range(12):
        linha.append(float(input()))
    vetor.append(linha)

for i in range(len(vetor)):
    for j in range(len(vetor)):
        if(i == L):
            soma += vetor[i][j]
            cont += 1
if(T.upper() == "S"):
    print(soma)
elif(T.upper() == "M"):
    print(soma / cont)