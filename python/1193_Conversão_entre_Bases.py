# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
casos = int(input())
for i in range(casos):
    numero,base = input().split()
    if base == 'bin':
          print('Case {}:'.format(i+1))
          print(((int(numero,2))),'dec')
          print(((hex(int(numero,2)))[2:]),'hex\n')
    elif base == 'dec':
        print('Case {}:'.format(i + 1))
        print(((hex(int(numero)))[2:]),'hex')
        print(((bin(int(numero)))[2:]),'bin\n')

    elif base == 'hex':
        print('Case {}:'.format(i + 1))
        print(int('0x' + numero,16),'dec')
        print(((bin(int(numero,16)))[2:]),'bin\n')