# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
n = list(map(int,input().split(" ")))
crescente = sorted(n)
for i in range(3):
    print(str(crescente[i]))

for i in range(3):
    if(i == 0):
        print("\n"+str(n[i]))
    else:
        print(str(n[i]))