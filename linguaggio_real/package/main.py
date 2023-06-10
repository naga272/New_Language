import maths
import fio
import re
import os


def main(file):
    if check_syntax_file(file): # verifico che il file ha estensione .by
        if os.path.exists(file): # verifico se il file esiste
            print("Il file corrisponde ed esiste")
            with open(file) as f_in:
                counter = 0 #contatore riga
                lista_funzioni = [] #lista che contiene tutte le funzioni che sono state incluse tramite "include"
                ''' CICLO PRINCIPALE DEL PROGRAMMA '''
                for line in f_in:
                    counter += 1 # dice a che riga mi trovo

                    ''' INCLUSIONE LIBRERIE '''
                    result = include(line, lista_funzioni, counter)
                    if result is not None:
                        lista_funzioni = result
                    if isinstance(lista_funzioni, str):
                        print(lista_funzioni)
                        return False
                    print(lista_funzioni)

                    ''' VARIABILI '''
                    variabile = check_sintax_var(line, counter)
                    print(variabile)
        else:
            print("programma inesistente")
    else:
        return False


def check_syntax_file(stringa):
    '''
        *
        * funzione che verifica la sintassi del nome del file
        *
    '''
    reg = re.compile(r"[A-Za-z]+[\d]*(\.by)$")
    if reg.match(stringa):
        return True
    return False


def include(line, lista_funzioni, counter):
    '''
        *
        * verifico che librerie vengono incluse per determinare le funzioni da usare.
        * Le funzioni vengono ritornate in una lista.
        * Le librerie devono avere la seguente struttura:
        * include <nomelibreria>\n  (opzionale il \n)
        *
    '''
    reg = re.compile(r"include\s<[A-Za-z]+>", re.VERBOSE)
    if reg.match(line) is not None:
        print(line)
        if line == "include <fio>\n":
            lista_funzioni = fio.fio(lista_funzioni)
            return list(set(lista_funzioni))
        elif line == "include <math>\n":
            lista_funzioni = maths.math(lista_funzioni)
            return list(set(lista_funzioni))
        else:
            return f'| error a riga {counter}: "{line}" -> syntax error |'
    else:
        return None


def check_sintax_var(line, count):
    '''
        *
        * funzione che verifica la creazione di una variabile.
        * al momento della creazione va assegnato un valore.
        * es:
        * var = 2
        *
    '''
    reg = re.compile(r'''
                    ^\s*                   
                    ([A-Za-z][\w]*)        
                    \s*=\s*                
                    (.*);$ 
                ''', re.VERBOSE)
    if reg.match(line):
        '''
            dalla riga rimuovo spazi bianchi e splitto =
            per avere a sinistra il nome var e a destra valore
            il return e' una lista => [variabile, valore]
        '''
        return line.replace(" ", "").replace("\n", "").replace(";", "").split("=")
    else:
        line = line.replace("\n", "")
        return f'| error a riga {count}: "{line}" -> syntax error |' # da completare


if __name__ == "__main__":
    main("sorgente.by")
