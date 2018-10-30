import numpy as np

def square(x):
    return x*x


def coulomb(x):
    return 1 / x


def CentralDifference(f, x, h):
    # f(x + h) - f(x - h)
    # ------------------   \approx f'(x)
    #       2*h
    return (f(x + h) - f(x - h))/(2*h)

