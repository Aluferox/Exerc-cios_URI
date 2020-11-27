# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import pow
vetor = []
N = int(input())
for i in range(N):
    X,Y = map(int,input().split(" "))
    Arafael =  pow((3*X),2)+pow(Y,2)
    Bbeto = 2*pow(X,2)+pow((5*Y),2)
    Ccarlos = ((-100 * X) + (pow(Y,3)))

    if(Arafael > Bbeto and Arafael > Ccarlos):
        vetor.append('Rafael ganhou')
    elif(Bbeto > Arafael and Bbeto > Ccarlos):
        vetor.append('Beto ganhou')
    else:
        vetor.append('Carlos ganhou')
for j in vetor:
    print(j)