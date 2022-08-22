# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
pares = 0
impares = 0
positivos = 0
negativos = 0
for i in range(5):
    N = int(input())
    if(N % 2 == 0 and N > 0):
        pares += 1
        positivos += 1
    elif(N % 2 == 0 and N < 0):
        pares += 1
        negativos +=1
    elif(N % 2 >= 1 and N > 0):
        impares += 1
        positivos += 1
    elif(N % 2 >= 1 and N < 0):
        impares += 1
        negativos += 1
    else:
        pares += 1

print(pares,"valor(es) par(es)")
print(impares,"valor(es) impar(es)")
print(positivos,"valor(es) positivo(s)")
print(negativos,"valor(es) negativo(s)")