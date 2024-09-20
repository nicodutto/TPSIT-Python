#Trovo il fattoriale di un numero inserito in input

num = int(input("Inserisci un numero: "))

def fattoriale(n):
    if n == 0:
        return 1
    else:
        return n * fattoriale(n - 1)

numFatt = fattoriale(num)   
print(f"Il fattoriale del numero inserito '{num}' è: {numFatt}.")