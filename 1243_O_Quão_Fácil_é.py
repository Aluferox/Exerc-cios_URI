# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

while True:
    try:

        a = input()

        b = a.split(' ')

        junta_palavras = ''
        numero_de_palavras = 0

        for i in b:
            if i.isalpha():
                junta_palavras += i
                numero_de_palavras += 1
            elif i[-1:] == '.':
                p = i[:-1]
                if p.isalpha():
                    junta_palavras += p
                    numero_de_palavras += 1
        try:
            if len(junta_palavras) // numero_de_palavras >= 4 and len(junta_palavras) // numero_de_palavras <= 5:
                print('500')
            elif len(junta_palavras) // numero_de_palavras >= 6:
                print('1000')
            else:
                print('250')
        except ZeroDivisionError:
            print('250')

    except EOFError:
        break