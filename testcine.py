import math
# teste da cinematica inversa

c = 180
q = 269

x = 400
y = 350
z = 50

mi = math.degrees(math.atan(x/y))
print(mi)
Lx = y/(1/(math.sin(math.radians(mi))))
print(Lx)
A = math.sqrt((z ** 2) + (Lx ** 2))
print(A)
alfa = math.degrees(math.atan(z / Lx))
print(alfa)
beta = math.degrees(math.acos(((A ** 2) + (c ** 2) - (q ** 2)) / (2 * A * c)))
print(beta)
T = alfa+beta
print(T)
