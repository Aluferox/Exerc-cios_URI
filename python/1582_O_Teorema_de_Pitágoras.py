# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
from math import pow
while True:
    try:
        def MDC(primo,primo1,primo2):
            cont = 1
            resultado = 0
            while(primo >= cont or primo1 >= cont or primo2 >= cont):
                if (primo % cont == 0 and primo1 % cont == 0 and primo2 % cont == 0):
                    resultado = cont
                cont += 1
            return resultado

        p1, p2, p3 = map(int, (input()).split(" "))
        mdc = MDC(p1,p2,p3)
        hiponusa = max(p1,p2,p3)
        tripla = pow(p1,2) + pow(p2,2) + pow(p3,2)
        hiponusa_2 = pow(hiponusa,2)

        if (hiponusa_2 == tripla - hiponusa_2):
            if(mdc == 1):
                print('tripla pitagorica primitiva')
            else:
                print("tripla pitagorica")
        if(hiponusa_2 != tripla - hiponusa_2):
            print('tripla')
    except:
        break