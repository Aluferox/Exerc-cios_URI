# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

entrada = map(float,input().split(' '))

entrada = list(entrada)
entrada.sort()

num1 = entrada[2]
num2 = entrada[1]
num3 = entrada[0]

if num1 >= (num2+num3):
    print('NAO FORMA TRIANGULO')
if num1**2 == (num2**2 + num3**2):
    print('TRIANGULO RETANGULO')
if num1**2 > (num2**2 + num3**2) and num1 < (num2+num3):
    print('TRIANGULO OBTUSANGULO')
if num1**2 < (num2**2 + num3**2):
    print('TRIANGULO ACUTANGULO')
if num1 ==num2 == num3:
    print('TRIANGULO EQUILATERO')
if num1 == num2 !=num3 or num1 == num3 !=num2 or num2 == num3 !=num1:
    print('TRIANGULO ISOSCELES')


