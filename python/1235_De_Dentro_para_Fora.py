# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

casos = int(input())

for i in range(casos):
    texto = input()
    tamanho = len(texto) // 2
    print(texto[:tamanho][::-1] + texto[tamanho:][::-1])