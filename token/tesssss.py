import re

# Definizione della regex per il costrutto "if"
if_pattern = r'\(\s*([\w+\s*[\+\-\*\%\/]*\s*[\w]+)\s*(!=|==|>=|<=|>|<)\s*([\w+\s*[\+\-\*\%\/]*\s*[\w]+)\s*\)\s*\?\s*{'

# Testo contenente il costrutto "if"
text = "(2 + 7 != a)?{"

# Cerca corrispondenze nella regex nel testo
match = re.search(if_pattern, text)

# Verifica se è stata trovata una corrispondenza
if match:
    print("Corrispondenza trovata!")
    print("Prima sezione:", match.group(1))
    print("Operatore di confronto:", match.group(2))
    print("Seconda sezione:", match.group(3))
else:
    print("Nessuna corrispondenza trovata.")

