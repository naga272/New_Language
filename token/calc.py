import re
from gestione_var import *


def rimuovi_elementi_vuoti(x):
    try:
        for i in range(0, len(x), 1):
            x.remove("")
        return x
    except Exception:
        return x


def risolvi_parentesi(numeri, operatori): # da completare
    i = 0
    stri = ''
    operatori_par = [] 
    numeri_par = []
    
    while operatori[i] != '(':
        stri += numeri[i] + operatori[i]
        i += 1

    i += 1
    while operatori[i] != ')':
        i += 1
    return EXIT_SUCCESS


def main(stri): #compile e match
    #pattern per requisiti stringa
    reg1 = re.compile(r"\s*\d+\s*[/*+%\-\(\)]*\s*\d+\s*")
    if reg1.match(stri):
        numeri = re.split(r"[/\*\-\+\s()%]\s*", stri) # lista numeri
        operatori = re.split(r"[\d\s]\s*", stri) # lista operatori / parentesi
        '''
            *
            *  Uso la funzione rimuovi_elementi_vuoti(x) per togliere dalle due liste gli elementi vuoti
            *  che si vanno a generare dal re.split()
            *
        '''
        numeri = rimuovi_elementi_vuoti(numeri) 
        operatori = rimuovi_elementi_vuoti(operatori)
        '''
            *
            * La lista numeri_par contiene tutti i numeri che sono all'interno delle parentesi
            * di un espressioni. La lista operatori_par contiene tutti gli operatori
            * che sono all'interno delle parentesi
            * di un espressioni
            *
        '''
        if "(" in operatori:
            risolvi_parentesi(numeri, operatori) # da completare
            return EXIT_SUCCESS
        return risolvi(numeri, operatori)
    else:
        return stri


def risolvi(numeri, operatori):
    while operatori != []:
        z = 0
        if '*' in operatori or '/' in operatori or '%' in operatori:
            while operatori[z] != '*' or operatori[z] != '/' or oroperatori[z] != '%': 
                if operatori[z] == '*':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) * int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break

                if operatori[z] == '/':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) // int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break

                if operatori[z] == '%':
                    operatori.remove(operatori[z])
                    numeri[z] = str(int(numeri[z]) % int(numeri[z + 1])) 
                    numeri.remove(numeri[z + 1])
                    break
                z += 1
        else:
            if operatori != []:
                if operatori[0] == '+':
                    operatori.remove(operatori[0])
                    numeri[0] = str(int(numeri[0]) + int(numeri[1]))
                    numeri.remove(numeri[1])

            if operatori != []:
                if operatori[0] == '-':
                    operatori.remove(operatori[0])
                    numeri[0] = str(int(numeri[0]) - int(numeri[1]))
                    numeri.remove(numeri[1])
    return int(numeri[0])


if __name__ == "__main__":
    x = "18 + 22 * 33 + 15 - 18 + 15"
    print(f"risultato di {x}: {main(x)}") #main("22 * 3 / 12 % 5")
