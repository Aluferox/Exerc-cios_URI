# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
vetor = []
while(True):
    try:
        S1 = (input().split(" "))
        n1 = int(S1[0])
        n2 = int(S1[1])
        miM = min(n1, n2)
        maX = max(n1, n2)
        print(maX - miM)
    except:
        break
for i in vetor:
    print(i)