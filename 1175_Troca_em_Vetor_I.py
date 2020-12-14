# -*- coding: utf-8 -*-

from random import randint

vetor = []

for i in range(20):
    vetor.append(int(input()))

for i , j in enumerate(vetor[::-1]):
    print("N["+str(i)+"] = "+str(j))