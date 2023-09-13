from compiler import *
from gestione_var import *
from regex import *
import calc
import re


def analisi_costrutto(stri):
    '''

    COSTRUTTO IF TEORICO
    (condizione)?{
        istruzioni...
    }

    '''

    try:
        stri = stri.replace(" ", "")
        stri = stri.replace("\t", "")
        stri = re.split(r'\n', stri)
        stri.remove("}")

        '''stri[0] ha sempre la condizione'''
        stri[0] = stri[0].replace(")?{", "")
        stri[0] = stri[0].replace("(", "")

        condizione = calc.rimuovi_elementi_vuoti(re.split("[A-Za-z\d%\+\*\-\(\)]", stri[0]))
        sezioni = calc.rimuovi_elementi_vuoti(re.split(condizione[0], stri[0]))
        number_sezione = calc.rimuovi_elementi_vuoti(re.split("[<>\+\-\*%/&=]*", sezioni[0]))
        operatori_sezione = calc.rimuovi_elementi_vuoti(re.split("[\dA-Za-z\n]+", sezioni[0]))
        number_sezione = scambio_var_value(number_sezione)
        sezioni[0] = calc.risolvi(number_sezione, operatori_sezione)
        number_sezione = scambio_var_value(calc.rimuovi_elementi_vuoti(re.split("[<>\+\-\*%/&=]*", sezioni[1])))
        operatori_sezione = calc.rimuovi_elementi_vuoti(re.split("[\dA-Za-z\n]+", sezioni[1]))

        if len(operatori_sezione) != 0:
            sezioni[1] = calc.risolvi(number_sezione, operatori_sezione)
        else:
            sezioni[1] = int(number_sezione[0])

        if condizione[0] == ">=":
            if sezioni[0] >= sezioni[1]:
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS]
            else:
                return [EXIT_SUCCESS]

        if condizione[0] == "<=":
            if sezioni[0] <= sezioni[1]:
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS]
            else:
                return [EXIT_SUCCESS]

        if condizione[0] == "==":
            if sezioni[0] == sezioni[1]:
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS, len(content_of_if)]
            else:
                return [EXIT_SUCCESS]

        if condizione[0] == "!=":
            if sezioni[0] != sezioni[1]:
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS, len(content_of_if)]
            else:
                return [EXIT_SUCCESS]

        if condizione[0] == ">":
            if sezioni[0] > sezioni[1]:
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS, len(content_of_if)]
            else:
                return [EXIT_SUCCESS]

        if condizione[0] == "<":
            print(sezioni)
            if int(sezioni[0]) < int(sezioni[1]):
                content_of_if = []
                for i in range(0, len(stri), 1):
                    if i > 0 and i < len(stri) - 1:
                        content_of_if.append(stri[i])
                counter = 0
                for codice in content_of_if:
                    if analisi_sorgente(codice, counter) == EXIT_FAILURE:
                        return [EXIT_FAILURE, len(content_of_if)] 
                    counter += 1
                return [EXIT_SUCCESS, len(content_of_if)]
            else:
                return [EXIT_SUCCESS]


    except Exception as e:
        #print(f" {e}")
        return [EXIT_FAILURE, 0]



'''
    
    WHILE TEORICO

    while(condizione_variabile...){
        istruzioni...
    }

'''

def analisi_while(stri):
    try:
        content_of_while = stri.split("\n")
        content_of_while = calc.rimuovi_elementi_vuoti(content_of_while)

        # content_of_while[0] contiene sempre la condizione
        content_of_while[0] = content_of_while[0].replace("while(", "")
        content_of_while[0] = content_of_while[0].replace("){", "")
        content_of_while[0] = content_of_while[0].replace(" ", "") 

        section = calc.rimuovi_elementi_vuoti(re.split("[>]", content_of_while[0]))

        section_left = section[0] # si riferisce alla parte di sinistra rispetto all'operatore logico (==, != ecc...) 
        section_right = section[1] # si riferisce alla parte di destra rispetto all'operatore logico (==, != ecc...) 

        section_left = re.findall(r'[a-zA-Z]+|\d+|\S', section_left) # splitto tutto quello che si trova all'interno della stringa
        section_right = re.findall(r'[a-zA-Z]+|\d+|\S', section_right) # splitto tutto quello che si trova all'interno della stringa
        
        #converto i nomi delle variabili nei valori effettivi

        section_right = scambio_var_value(section_right) 
        section_left = scambio_var_value(section_left) # funzione definita in gestione_var.py

        if len(section_left) % 2 == 0 or len(section_right) % 2 == 0: # controllo errori nella definizione della condizione
            return [EXIT_FAILURE, len(content_of_while)]
        

        risultato_sinistra = ''
        for element in section_left:
            risultato_sinistra += element

        risultato_sinistra = calc.main(risultato_sinistra)

        risultato_destra = ''        
        for element in section_right:
            risultato_destra += element
        risultato_destra = calc.main(risultato_destra)

        operatore = calc.rimuovi_elementi_vuoti(re.search(r"([<>=!]=|[<>])", content_of_while[0]))[0]
        
        if operatore == ">":
            index_while = 1
            while int(risultato_sinistra) > int(risultato_destra):
                
                if analisi_sorgente(content_of_while[index_while], index_while) == EXIT_FAILURE:
                    return [EXIT_FAILURE, len(content_of_while)]       
                
                if index_while == len(content_of_while) - 1:
                    index_while = 1
                else:
                    index_while += 1

                print(content_of_while[index_while])
                print(variabili_del_sorgente)
        return [EXIT_SUCCESS, len(content_of_while)]
    
    except Exception as e:
        #print(f"syntax error:\n{e}")
        return [EXIT_FAILURE, len(content_of_while)]
