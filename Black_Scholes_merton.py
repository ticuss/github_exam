import numpy as np
import math

S = 1
X = 3
T = 5
R = 0.50
OMEGA = 20
N = 5


def d_one(
    S,
    X,
    R,
    OMEGA,
    T,
):
    calc = ((np.log(S / X)) + (R + OMEGA**2) * T) / OMEGA * math.sqrt(T)
    return calc


def d_two(
    S,
    X,
    R,
    OMEGA,
    T,
):
    d1 = d_one(
        S,
        X,
        R,
        OMEGA,
        T,
    )
    calc = d1 - OMEGA * math.sqrt(T)
    return calc


def c():
    d1 = d_one(
        S,
        X,
        R,
        OMEGA,
        T,
    )
    d2 = d_two()
    res = S * N(d1) - X ** math.exp(-R * T) * N(d2)
    return res


def p():
    d1 = d_one(
        S,
        X,
        R,
        OMEGA,
        T,
    )
    d2 = d_two()
    res = X * math.exp(-R * T) * N * (-d2) - S * N(-d1)
