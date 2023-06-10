# New Language

![Language](https://img.shields.io/badge/Spellcheck-Pass-green?style=flat)
![Platform](https://img.shields.io/badge/OS%20platform%20supported-Windows-blue?style=flat)

## Descrizione

Programma che dato il file sorgente con estensione .by analizza il suo contenuto. 
Verifica se la sintassi del codice sorgente contenuto nel programma .by rispetti un certo pattern.
il programma .by può contenere le seguenti istruzioni:

- #include <fio> 
- #include <math>
- var = 4

l'output del programma sorgente.by inserendo:
include <fio>
include <math>

variabile = 5

sarà il seguente:


Il file corrisponde ed esiste
include <fio>

['scanf', 'printf', 'fopen', 'rmdir', 'mkdir']
| error a riga 1: "include <fio>" -> syntax error |
include <math>

['pow', 'scanf', 'tan', 'cotan', 'log', 'printf', 'cos', 'sin', 'fopen', 'rmdir', 'sqrt', 'mkdir']
| error a riga 2: "include <math>" -> syntax error |

['pow', 'scanf', 'tan', 'cotan', 'log', 'printf', 'cos', 'sin', 'fopen', 'rmdir', 'sqrt', 'mkdir']
| error a riga 3: "" -> syntax error |

['pow', 'scanf', 'tan', 'cotan', 'log', 'printf', 'cos', 'sin', 'fopen', 'rmdir', 'sqrt', 'mkdir']
| error a riga 4: "variabile = 5" -> syntax error |
## Requisiti

IDE python

## Author

Bastianello Federico
