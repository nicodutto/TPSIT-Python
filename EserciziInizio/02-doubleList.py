# Da lista1 = [1, 2, 3, 4, 5], creo lista2 che ha tutti i valori raddoppiati

lista1 = [1, 2, 3, 4, 5]    #lista da raddoppiare
lista2 = []
for item in lista1:
    lista2.append(item * 2)
    
print(lista2)