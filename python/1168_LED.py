# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
T = int(input())
vetor = []
for i in range(T):
    soma = 0
    numero = list(map(int, input()))
    for j in range(len(numero)):
        if numero[j] == 1:
            soma += 2
        elif(numero[j] == 4):
            soma += 4
        elif(numero[j] == 7):
            soma += 3
        elif(numero[j] == 8):
            soma += 7
        elif(numero[j] == 2 or numero[j] == 3 or numero[j] == 5):
            soma += 5
        elif(numero[j] == 0 or numero[j] == 6 or numero[j] == 9):
            soma += 6
    vetor.append(soma)
    numero =None

for i in vetor:
    print(i, 'leds')