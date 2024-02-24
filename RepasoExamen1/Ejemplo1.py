# Ejemplo de herencia
class Animal:
    def hablar(self):
        print("Haciendo sonidos")

class Perro(Animal):
    def hablar(self):
        print("Ladrando")

class Lobo(Animal):
    def hablar(self):
        print("Auyando")

perro = Perro()
perro.hablar()  # Salida: "Ladrando"

lobo = Lobo()
lobo.hablar()