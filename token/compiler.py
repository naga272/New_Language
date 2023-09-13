from gestione_var import *
from costrutti import *
from regex import *
import argparse
import calc
import re



def main(file):
    with open(file, "r") as sorgente:
        counter = 1 # contatore linea
        flag_ricordo = 0
        ricordo_contenuto_if = ""
        ricordo_contenuto_while = ""
        for lines in sorgente: # CICLO PRINCIPALE

            ''' COSTRUTTO IF '''
            if esperimento_if_start.match(lines):
                flag_ricordo = 1
            if flag_ricordo == 1: 
                ricordo_contenuto_if += lines
            if reg_x_if_costrutto_end.match(lines):
                flag_ricordo = 0
                if analisi_costrutto(ricordo_contenuto_if) == EXIT_FAILURE:
                    print(f"error syntax start: {counter - analisi_costrutto(ricordo_contenuto_if)[1]}: --> \n{ricordo_contenuto_if}") 
                    return EXIT_FAILURE
                else:
                    ricordo_contenuto_if = ''

            ''' COSTRUTTO WHILE '''
            if reg_x_while_start.match(lines):
                flag_ricordo = 1
            if flag_ricordo == 1:
                ricordo_contenuto_while += lines
            if reg_x_while_end.match(lines):
                flag_ricordo = 0
                if analisi_while(ricordo_contenuto_while) == EXIT_FAILURE:
                    print(f"|__ error syntax start: {counter - analisi_while(ricordo_contenuto_while)[1]}: --> \n{ricordo_contenuto_while} __|") 
                    return EXIT_FAILURE
                else:
                    ricordo_contenuto_while = ''

            ''' CODICE BASE, KEY = VALUE '''
            if flag_ricordo == 0 and not reg_x_if_costrutto_end.match(lines):
                if analisi_sorgente(lines, counter) == EXIT_FAILURE: # caso in cui ritorna EXIT_FAILURE, analisi sorgente si trova in gestione_var.py
                    lines = lines.replace("\n", "")
                    print(f"-- Error syntax at line {counter} --> {lines} --")
                    break
            counter += 1
        print(f'\n\nvariabili_del_sorgente: {variabili_del_sorgente}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help='inserire percorso file .byn')
    args = parser.parse_args()
    main(args.file) # inizio programma
