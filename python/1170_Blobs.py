# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
t= int(input())
dias = []
cont = 0
for i in range(t):
    quantidade = float(input())
    while(quantidade > 1):
        quantidade /= 2
        cont += 1
    dias.append(cont)
    cont = 0
for j in dias:
    print(j,'dias')