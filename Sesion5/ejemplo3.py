#listas
lista = [1, 2, 3, "Manzana", 15.6, True, False]
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

#imprimir los ultimos tres elementos de la lista
final = len(lista)
inicio = final - 3
print(lista[inicio: final +1])

#eliminar manzana
lista.remove("Manzana")
lista.remove("Roberto")

#ordenar lista
lista.sort()
print(lista)