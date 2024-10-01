import math
import sympy as sp
import numpy as np

x, y = sp.symbols('x y')

#number of polynomials
n = m = 10

#Geometrical properties
a, b = 8, 8
h = 0.01

#mechanical properties
E = 1
nu = 0.3
D = (E*h**3)/(12*(1-nu**2))

#Pmn
def P(m, n):
    return (4/(a*b))*( sp.integrate(sp.sin( (m*math.pi*x)/(a) ), (x, 0, a)) * sp.integrate(sp.sin( (n*math.pi*y)/b ), (y, 0, b)) )

#Wmn
def W(m, n):
    return P(m,n)/( D*(math.pi**4)*( (m/a)**2 + (n/b)**2 )**2 )

Wmn = 0
for i in range(1, m):
    for j in range(1, n):
        Wmn += W(i, j)

#Deflection at x=a/2 and y=b/2
print(Wmn)