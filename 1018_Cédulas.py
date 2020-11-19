# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

notas = [100, 50, 20, 10, 5, 2, 1]
total_notas = int(input())

print(total_notas)
for i in notas:
    print("{quantidade} nota(s) de R$ {valor},00".format(quantidade=total_notas//i, valor=i))
    total_notas = total_notas%i