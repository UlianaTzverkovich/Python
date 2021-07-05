import math
class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def vector(point1, point2):
    vector = math.sqrt(pow((point2.y - point1.y), 2) + pow((point2.x - point1.x), 2))
    return vector

def trgl_square(a, b, c):
    p = (a + b + c) / 2
    square = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return square

A = point(0.6,1.4)
B = point(1.3,0.9)
C = point(2,1.4)
D = point(1.7,2.2)
E = point(0.9,2.2)

AB = vector(A, B)
AC = vector(A, C)
CD = vector(C, D)
DE = vector(D, E)
EC = vector(E, C)
AE = vector(A, E)
BC = vector(B, C)

ABC_square = trgl_square(AB, BC, AC)
CDE_square = trgl_square(CD, DE, EC)
ACE_square = trgl_square(EC, AE, AC)

fvgl_square = round((ABC_square + CDE_square + ACE_square), 2)

print("Площадь выпуклого пятиугольника = {0}".format(fvgl_square))