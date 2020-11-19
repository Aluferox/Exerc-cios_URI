# -*- coding: utf-8 -*-
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

from difflib import SequenceMatcher
while True:
    try:
       string1 = input()
       string2 = input()

       resultado = SequenceMatcher(None, string1, string2)
       print(resultado.find_longest_match(0, len(string1), 0, len(string2)).size)

    except EOFError:
        break