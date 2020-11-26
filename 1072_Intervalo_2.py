# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
tentativas = int(input())

dentro = []
cont_dentro = 0
cont_fora = 0
for i in range(tentativas):
    n = int(input())
    if n >= 10 and n <= 20:
        cont_dentro += 1
    else:
        cont_fora += 1
print(cont_dentro,'in')
print(cont_fora,'out')