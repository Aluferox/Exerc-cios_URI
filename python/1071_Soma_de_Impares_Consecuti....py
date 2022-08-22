# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
N = int(input())
N1 = int(input())
soma = 0
min = min(N,N1)
max = max(N,N1)
for i in range((min+1),max):
    if(i % 2 != 0):
        soma += i
print(soma)
