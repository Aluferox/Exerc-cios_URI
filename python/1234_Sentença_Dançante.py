# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
    def junta_String(f):
        b = ''
        cont = 0
        for i in f:
            if i.isalpha():
                if cont % 2 == 0:
                    b += i.upper()
                    cont += 1
                else:
                    b += i.lower()
                    cont += 1
            else:
                b += i
        return b

    try:
        a = input()
        print(junta_String(a))
    except EOFError:
        break




