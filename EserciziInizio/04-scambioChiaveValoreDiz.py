# Dizionario: {"a": 1, "b": 2, "c": 3}, scambio la posizione tra chiave e valore

# Dizionario originale
dizionario = {'a': 1, 'b': 2, 'c': 3}

# Scambio chiavi e valori
dizionario_invertito = {valore: chiave for chiave, valore in dizionario.items()}

# Stampa del dizionario invertito
print(dizionario_invertito)
