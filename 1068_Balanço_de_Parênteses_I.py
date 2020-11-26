# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
while True:
     try:
        def teste(c):
            contAberto = 0
            contFechado = 0
            for c in a:
                if c == '(':
                    contAberto += 1
                elif c == ')':
                    contFechado += 1

                if contFechado > contAberto:
                    return 'incorrect'

            #print(contFechado, contAberto)
            if contAberto == contFechado:
                return 'correct'
            else:
                return 'incorrect'
        a = input()
        print(teste(a))
     except EOFError:
        break