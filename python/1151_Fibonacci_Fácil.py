# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
fibo = int(input())

aux = 1
aux2 = 0
anterior = [0,1]
for i in range(1,fibo):
    if i == 1:
        continue
    else:
        aux += aux2
        aux2 = aux - aux2
        anterior.append(aux)
result = ''
for result_fibo in anterior:
    result += str(result_fibo)+' '
print(result.rstrip())