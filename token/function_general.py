from regex import *
import calc


EXIT_SUCCESS = 0
EXIT_FAILURE = 1


'''
    FUNCTION_LIST
    contiene la lista di funzioni di default
'''


def is_function(key):
    if printf(key) == EXIT_SUCCESS:
        return EXIT_SUCCESS
    else:
        return EXIT_FAILURE


def printf(stri):
    '''
        funzione printf()
        nella funzione printf si puo passare coma paramentro una stringa o una singola variabile o
        un numero alla volta 
    '''
    if reg_x_printf_function.match(stri):
        key = preleva_contenuto_par(stri) 
        
        if reg_is_digit.match(key):     # printf(11)
            print(int(key))
            return EXIT_SUCCESS

        if reg_is_str.match(key):       # printf("Hello World") -> Hello World
            str_content = ""
            for i in range(1, len(key) - 1, 1):
                str_content += key[i]
            print(str_content)
            return EXIT_SUCCESS

        if re.compile(CASE_VAR).match(key):       # printf(a) -> a è una variabile
            if key in variabili_del_sorgente:                
                print(variabili_del_sorgente[key])
                return EXIT_SUCCESS
            else:
                print(f"-- Error, undeclared variable \"{key}\" --")
                return EXIT_FAILURE

        if reg_x_printf_function.match(stri): #se c'è all'interno un'altra printf da errore
            return EXIT_FAILURE

    return EXIT_FAILURE


def preleva_contenuto_par(stri):
    '''
        funzione che consente di ottente il codice che sta all'interno delle parentesi tonde
        printf("ciao") ritorna: "ciao"
    '''
    inizio = stri.find("(")
    fine = stri.find(")")
    
    if inizio == -1 or fine == -1 or fine < inizio:
        return None
    
    contenuto = stri[inizio + 1 : fine]
    contenuto = contenuto.strip()  # Rimuove spazi iniziali e finali
    return contenuto
