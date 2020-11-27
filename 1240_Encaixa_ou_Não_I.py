# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
teste = int(input())
vetor = []
for i in range(teste):
    n1,n2 = map(str,input().split())
    mim = len(n1)
    maX = len(n2)
    mim1 = min(mim,maX)
    maX1 =max(mim,maX)

    if(len(n1) > len(n2)):
        tamanho = maX1 - mim1
        n3 = n1[tamanho:]
        if(n2 == n3):
            vetor.append('encaixa')
        else:
            vetor.append('nao encaixa')
    elif(len(n1) == len(n2)):
        if(n1 == n2):
            vetor.append('encaixa')
        else:
            vetor.append('nao encaixa')
    else:
        vetor.append('nao encaixa')
for i in vetor:
    print(i)