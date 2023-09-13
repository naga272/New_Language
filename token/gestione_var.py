from regex import *
from function_general import *
import calc


'''
    *
    * EXIT_SUCCESS e EXIT_FAILURE sono originariamente usate nel linguaggio C (dichiarate all'interno
    * della libreria stdlib.h) che possono rappresentare lo stato True / False
    * La costante EXIT_SUCCESS ha valore 0, EXIT_FAILURE ha valore != 0 
    *
'''

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def scambio_var_value(lista):
    for i in range(0, len(lista), 1):
        if reg_is_var.match(lista[i]):
            if lista[i] in variabili_del_sorgente:
                lista[i] = variabili_del_sorgente[lista[i]]
    return lista


def assegnazione(stri, counter): # assegnazione variabili
    try:
        #tipi di variabili creabili: interi e stringhe, possibile somma tra interi
        
        if "=" in stri:
            if reg_x_syntax_var.match(stri) or reg_x_syntax_var_x_str.match(stri): # key = value # PROBLEMA CON STRINGHE
                suddivisore = stri.replace(" ", "")
                suddivisore = suddivisore.replace("\n", "")
                suddivisore = re.split("=", suddivisore)
                '''
                    *
                    *   suddivisore[0] contiene il nome della variabile
                    *   suddivisore[1] contiente il valore della variabile
                    *
                '''
                if len(suddivisore) == 2:
                    
                    if reg_is_str.match(suddivisore[1]): # caso di assegnazione stringa                        
                        suddivisore = stri
                        suddivisore = re.split("=", stri)
                        suddivisore[0] = suddivisore[0].replace(" ", "")
                        suddivisore[1] = rimuovi_spazi_corretti(suddivisore[1])
                        print(suddivisore[1])
                        variabili_del_sorgente[suddivisore[0]] = suddivisore[1]

                    if reg_x_calcoli_aritmetici.match(suddivisore[1]): # es: 4 +2 -5 * 88
                        suddivisore[1] = str(calc.main(suddivisore[1]))

                    if reg_x_calcoli_var_to_num.match(suddivisore[1]):  # es: 22 + c * a - 5 / d  
                        context = re.split(r"[/\*\-\+\s()%]\s*", suddivisore[1])
                        operandi = calc.rimuovi_elementi_vuoti(re.split(r"[\dA-Za-z]+", suddivisore[1]))
                        i = 0
                        for variable in context:
                            if variable in variabili_del_sorgente:
                                context[i] = variabili_del_sorgente[variable]
                            i += 1
                        suddivisore[1] = str(calc.risolvi(context, operandi))
                        variabili_del_sorgente[suddivisore[0]] = suddivisore[1]

                    if reg_x_calcoli_aritmetici_tra_var.match(suddivisore[1]): #es: a = b - c
                        context = re.split(r"[/\*\-\+\s()%]\s*", suddivisore[1])
                        operandi = calc.rimuovi_elementi_vuoti(re.split(r"[\dA-Za-z]+", suddivisore[1]))
                        i = 0
                        for variable in context:
                            if variable in variabili_del_sorgente:
                                context[i] = variabili_del_sorgente[variable]
                            i += 1
                        suddivisore[1] = str(calc.risolvi(context, operandi))
                        variabili_del_sorgente[suddivisore[0]] = suddivisore[1]
                        return EXIT_SUCCESS

                    if reg_x_take_function.match(suddivisore[1]): #es : a = funzione() # da finire
                        suddivisore[1] = suddivisore[1].split("(")
                        print(suddivisore)

                    if reg_x_assegnazione_var.match(suddivisore[1]): # es: a = b
                        if suddivisore[1] in variabili_del_sorgente:
                            suddivisore[1] = variabili_del_sorgente[suddivisore[1]]
                            variabili_del_sorgente[suddivisore[0]] = suddivisore[1]
                        else:
                            return EXIT_FAILURE

                    variabili_del_sorgente[suddivisore[0]] = str(calc.main(suddivisore[1])) 
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
        return EXIT_FAILURE
    except Exception as e:
        #print(f'{e}')
        return EXIT_FAILURE


def analisi_sorgente(stri, counter):
    '''
        funzione che prende riga per riga del file sorgente e la analizza
        EXIT_SUCCESS e EXIT_FAILURE sono inizializzate nella libreria gestione_var.py
    '''
    
    if assegnazione(stri, counter) == EXIT_SUCCESS: #libreria gestione_var
        return EXIT_SUCCESS #evito di fare tutti i comandi se si tratta di una assegnazione la stringa corrente

    elif reg_x_line_vuota.fullmatch(stri): # linea vuota
        return EXIT_SUCCESS

    elif reg_x_comment.search(stri): # caso commento
        return EXIT_SUCCESS

    elif reg_x_printf_function.match(stri): # caso funzione printf
        if printf(stri) == EXIT_FAILURE:
            return EXIT_FAILURE
        return EXIT_SUCCESS

    else:
        return EXIT_FAILURE # nessun comando corrisponde a questa sintassi


def rimuovi_spazi_corretti(stri):
    # "ciao mondo" --> "ciao mondo"
    match = re.search(r'"[^"]*"', stri)
    return match.group()
