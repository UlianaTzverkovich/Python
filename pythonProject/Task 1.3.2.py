import math
import numpy

m = int(input("Кол-во строк: "))
n = int(input("Кол-во столбцов: "))
x = []
for X in range(1, m + 1):
    for Y in range(1, n + 1, 1):
        x.append(pow(X, Y))

x = numpy.reshape(x, (m, n))
print(x)