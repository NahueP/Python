from math import sqrt
import math

numA = int(input('Ingrese numero A: '))
numB = int(input('Ingrese numero B: '))
numC = int(input('Ingrese numero C: '))

x1=0;
x2=0;

if((numB**2)-(4*numA*numC))<0:
    print('No se puede realizar la operacion')
else:
    x1 = ((-numB)+((sqrt(pow(numB,2))-(4*numA*numC))/2*numA))
    x2 = ((-numB)-((sqrt(pow(numB,2))-(4*numA*numC))/2*numA))
    print("Solucion x1:", x1)
    print("Solucion x2:", x2)


