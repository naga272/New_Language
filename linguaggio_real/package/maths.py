import math

'''
    *
    * libreria maths.py
    * funzioni matematiche
    *
'''

def math(lista):
    lista.append("sqrt")
    lista.append("pow")
    lista.append("log")
    lista.append("cos")
    lista.append("sin")
    lista.append("tan")
    lista.append("cotan")
    return lista


def ssqrt(x):
    return math.sqrt(x)


def ppow(x, n):
    return pow(x, n)

