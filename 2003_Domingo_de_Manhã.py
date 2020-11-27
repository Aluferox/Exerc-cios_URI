# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    try:
        soma = 0
        h,m = map(int,input().split(":"))
        if(h >= 5 and h <= 6 and m <=59):
            print('Atraso maximo:',soma)
        elif(h == 7 and m <= 59):
            print('Atraso maximo:',m)
        elif(h == 8):
            print('Atraso maximo:',m+60)
        elif(h == 9):
            print('Atraso maximo:',120)
    except:
        break