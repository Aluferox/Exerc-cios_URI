cont = None
numero = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


cont = 0
for count in range(6):
  numero = read_numeric()
  if numero > 0:
    cont = cont + 1
print(str(cont) + str(" valores positivos"))
