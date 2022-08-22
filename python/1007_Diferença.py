A = None
B = None
C = None
D = None
diferenca = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

A = read_integer()
B = read_integer()
C = read_integer()
D = read_integer()
diferenca = A * B - C * D

print(str("DIFERENCA = ") + str(diferenca))