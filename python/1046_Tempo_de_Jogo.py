# -*- coding: utf-8 -*-

import datetime

horaInicial, horaFinal = input().split(' ')

tempo = datetime.timedelta(hours=int(horaFinal)) - datetime.timedelta(hours=int(horaInicial))

if str(tempo).split(':')[0] != '0':
    print('O JOGO DUROU {horas} HORA(S)'.format(horas=str(datetime.timedelta(seconds=tempo.seconds)).split(':')[0]))
else:
    print('O JOGO DUROU 24 HORA(S)')
