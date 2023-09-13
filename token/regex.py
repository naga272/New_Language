import re

''' variabili_del_sorgente contiene tutte le variabili con i relativi valori del programma sorgente '''

variabili_del_sorgente = {

}

# caso che la riga non contiene caratteti ma spazi o \n
reg_x_line_vuota = re.compile(r'([\s]+)|\n') 


''' REGOLE PER I COMMENTI DEL SORGENTE '''
reg_x_comment = re.compile(r'\/\/\s*.*(?:\n|$)')


''' REGOLE PER ASSEGNAZIONE E CREAZIONE VARIABILI'''
reg_x_syntax_var = re.compile(r'[\t\s]*[A-Za-z]+[\t\s]*[=]{1}[\t\s]*[A-Za-z\d\s\t+-\.\*\\\,\(\)]+') # key = value
reg_x_syntax_var_x_str = re.compile(r'[\t\s]*([A-Za-z]+)[\t\s]*=[\t\s]*"(.*?)"[\t\s\n]*') # var = "stringa"
reg_x_assegnazione_var = re.compile(r'[A-Za-z\_]+[\dA-Za-z\_]*')          # es: a = b
reg_x_calcoli_aritmetici = re.compile(r"\s*\d+\s*[/*+%\-\(\)]*\s*\d+\s*") # es: 4 +2 -5 * 88
reg_x_calcoli_aritmetici_tra_var = re.compile(r"\s*([A-Za-z]+[\dA-Za-z]*)\s*([\+\*-/%]{1}[\dA-Za-z]+)+\s*") # es: a = b + c
reg_x_calcoli_var_to_num = re.compile(r"\b(\d+\s*[-+*/%]\s*(?:\d+|[A-Za-z]+\d*)\s*)\b") # es: a * b + 12
reg_is_var = re.compile(r'[A-Za-z]+[A-Za-z\d\_]*') # check name var
reg_is_digit = re.compile(r'[\d]+') # check numeri
reg_is_str = re.compile(r'[\t\s]*"(.*?)"[\t\s\n]*') # es: a = "assegno la stringa ad a", il . rappresenta un qualsiasi carattere


''' ASSEGNAZIONE FUNZIONI ALLE VARIABILI '''
reg_x_take_function = re.compile(r"([A-Z]+[\(][A-Za-z])*([,][\d|[A-Za-z\d])*([\)])+") # es a = funzione()


''' COSTRUTTO IF '''

first_section_if = r'\(\s*([\w+\s*[\+\-\*\%\/]*\s*[\w]+)\s*'
second_section_if = r'(!=|==|>=|<=|>|<)\s*'
third_section_if = '([\w+\s*[\+\-\*\%\/]*\s*[\w]+)\s*\)\s*\?\s*{'

esperimento_if_start = re.compile(first_section_if + second_section_if + third_section_if)

reg_x_if_costrutto_start = re.compile(r'\s*\(\s*[A-Za-z\d<>\+\-\*%/&=\s!]+\s*\)\?\s*{\s*\n*') # start-if + condizione
reg_x_if_costrutto_end = re.compile(r'\s*}\s*\n*') # end if


''' 

    COSTRUTTO WHILE

    while(condizione){
        istruzione

    }

'''
condizione = r'\s*[A-Za-z\d<>\+\-\*%/&=\s!]+\s*'
swhile = r'\s*while\s*\(' + condizione + '\)\s*{\s*\n*'
reg_x_while_start = re.compile(swhile)
reg_x_while_end = reg_x_if_costrutto_end


''' 

    FUNZIONE PRINTF 
    
    printf("ciao")
    printf(11)
    printf(variabile)
    printf(funzione())
    printf(funzione(a))
    printf(funzione(11, "ciao"))

'''
OR = r'|'
START_CASE = r'\s*printf\s*\('
    
CASE_VAR = r'(\s*[A-Za-z\_]+[\w]*\s*)'
CASE_STR = r'(\s*"[^"]*")'
CASE_NUM = r'(\d*)'
three_case = f'({CASE_VAR}|{CASE_STR}|{CASE_NUM})'

PARAMETRI_FUNCTION = f'({three_case}(,\s*{three_case})*)*'  #(1, 2)
CASE_FUNCTION = r'(\s*[A-Za-z\_]+[\w]*\s*\(' + PARAMETRI_FUNCTION + '\))' # function()

END_CASE = r'\)\s*\n*' # rappresenta la fine della printf; 

reg_x_printf_function = START_CASE + "(" + three_case + OR + CASE_FUNCTION + ")" + END_CASE
reg_x_printf_function = re.compile(reg_x_printf_function)


''' CARATTERISTICHE FUNZIONE GENERALE '''
reg_is_function = re.compile(f'{CASE_FUNCTION}') # sintassi di una qualunque funzione
