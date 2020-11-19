# -*- coding: utf-8 -*-

from math import sqrt, pow

x1y1 = input().split(' ')
x2y2 = input().split(' ')
x1y1 = [float(i) for i in x1y1]
x2y2 = [float(i) for i in x2y2]

print('{:.4f}'.format(sqrt(pow(x2y2[0]- x1y1[0],2) + pow(x2y2[1] - x1y1[1], 2))))