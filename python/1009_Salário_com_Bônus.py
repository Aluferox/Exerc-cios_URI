# -*- coding: utf-8 -*-

nome = input()
salario = float(input())
vendas = float(input())

print('TOTAL = R$ {:.2f}'.format((vendas * 0.15) + salario))