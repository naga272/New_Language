'''
    *
    * libreria fio.py
    * fio sta per function input-output.
    *
'''

def fio(lista):
    lista.append("printf")
    lista.append("scanf")
    lista.append("fopen")
    lista.append("mkdir")
    lista.append("rmdir")
    return lista


def printf(x):
    print(x)


def scanf(x):
    x = input("")
    return x
