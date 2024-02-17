#listas
lista = [1, 2, 3, "Manzana", 15.6, True]
print(lista)

#imprimir el primer elemento de la lista
print(lista[0])

#tamano de la lista
tam = len(lista)
print(f"El tamano es {tam}")

#imprimir el ultimo valor
print(lista[tam-1])

#imprimir los elementos 4 hasta 6
print(lista[3:7])

#agregar un elemento a la lista
lista.append("Roberto")
print(lista)