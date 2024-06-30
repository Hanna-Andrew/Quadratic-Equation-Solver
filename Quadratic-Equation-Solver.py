# 2nd order equation solver ax^2+bx+c=0
import math
a = float(input("Inserisci a: "))
b = float(input("Inserisci b: "))
c = float(input("Inserisci c: "))

if(a==0):
  print("L'equazione è di 1 grado!")
  if(b!=0):
    x=-c/b
    print("La soluzione è x=", str(x))
  elif(b==0 and c==0):
    print("L'equazione è indeterminata")
  elif(b==0 and c!=0):
    print("l'equazione è impossibile")
else:
  delta = b**2-4*a*c

  if(delta==0):
    x1 = (-b)/(2*a)
    print("L'equazione ha 2 soluzioni coincidenti x=", str(x1))
  elif(delta<0):
    print("l'equazione non ha soluzioni reali")
  else:
    x1 = (-b+math.sqrt(delta))/(2*a)
    x2 = (-b-math.sqrt(delta))/(2*a)
    print("L'equazione ha 2 soluzioni x1=" + str(x1) + " e x2=" + str(x2))
