# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor_sequencia = []
vetor_soma = []

while(True):
    soma = 0
    linha = []
    x1, x2 = list(map(int,input().split(" ")))
    if(x1 == 0 or x1 < 0 or x2 == 0 or x2 < 0):
        break
    menor = min(x1,x2)
    maior = max(x1,x2)
    for i in range(menor,maior+1):
        linha.append(i)
    vetor_soma.append(sum(linha))
    grupo = " ".join(map(str, linha))
    vetor_sequencia.append(grupo)

for i,j in zip(vetor_sequencia,vetor_soma):
    print(i , "Sum="+str((j)))





