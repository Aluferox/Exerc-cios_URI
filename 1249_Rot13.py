# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

import string
while True:
    try:
        palavra_secreta = input()
        def rot13(letra):
               if letra.islower():
                   if len(string.ascii_lowercase) //2 <= string.ascii_lowercase.index(letra):
                       return string.ascii_lowercase[(string.ascii_lowercase.index(letra) + 13) - len(string.ascii_lowercase)]
                   else:
                       return string.ascii_lowercase[string.ascii_lowercase.index(letra) +13]
               else:
                   if len(string.ascii_uppercase) //2 <= string.ascii_uppercase.index(letra):
                       return string.ascii_uppercase[(string.ascii_uppercase.index(letra) + 13) - len(string.ascii_uppercase)]
                   else:
                       return string.ascii_uppercase[string.ascii_uppercase.index(letra) +13]

        criptografia = ''
        for letra in palavra_secreta:
            if letra.isalpha():
                criptografia +=rot13(letra)
            else:
                criptografia += letra
        print(criptografia)
    except EOFError:
        break