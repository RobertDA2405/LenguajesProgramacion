import math

#calcular el area de un circulo
radio = int(input("Ingrese el radio del círculo: "))
area = math.pi * pow(radio, 2)
#imprimir el resultado con dos decimales
print("El area del círculo es: (:.2f)".format(area))