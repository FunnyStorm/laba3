from math import *
from random import *

def vivod(x1, x2, dx):
    xc = x1
    print('+--------+--------+')
    print('I    X   I    Y   I')
    print('+--------+--------+')
    while xc <= x2:
        if -9 <= xc <= -6:
            y = -sqrt(9-(xc+6)**2)
        elif -6 < xc <=-3:
            y = xc+3
        elif -3 < xc <= 0:
            y = sqrt(9-xc**2)
        elif 0 < xc <=3:
            y = 3 - xc
        else:
            y = (xc-3)/2
        print('I{0: 7.2f} I{1: 7.2f} I'.format(xc, y))
        xc += dx
    print('+--------+--------+')

def main():
    x1 = float(input('Xbeg = '))
    x2 = float(input('Xend = '))
    dx = float(input('DX = '))

    vivod(x1, x2, dx)

if __name__ == "__main__":
    main()

