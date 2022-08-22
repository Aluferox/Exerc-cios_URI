# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
anterior = 0
atual = 1
vetor = [0,1]

for i in range(61):
   atual += anterior
   anterior = atual - anterior
   vetor.append(atual)

T = int(input())
for i in range(T):
    N = int(input())
    print("Fib("+str(N)+") = "+str(vetor[N]))