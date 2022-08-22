# -*- coding: utf-8 -*-

import  datetime
horaInicial, minutoInicial, horaFinal, minutoFinal = map(int, (input().split(' ')))

tempo = datetime.timedelta(hours=horaFinal, minutes=minutoFinal) - datetime.timedelta(hours=horaInicial, minutes=minutoInicial)

if str(tempo) != '0:00:00':
    if 'day' in str(tempo):
        hora, mim = map(int, str(tempo)[8:].split(':')[:2])
        print('O JOGO DUROU {hora} HORA(S) E {mim} MINUTO(S)'.format(hora=hora, mim=mim))

    else:
        hora, mim = map(int, str(tempo).split(':')[:2])
        print('O JOGO DUROU {hora} HORA(S) E {mim} MINUTO(S)'.format(hora=hora, mim=mim))

if horaInicial == horaFinal and minutoInicial == minutoFinal:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')