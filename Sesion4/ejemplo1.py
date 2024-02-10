class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear objeto persona
persona1 = Persona("Roberto", 18)
persona1.saludar()

# Mama
mama = Persona("Arlen", 40)
mama.saludar()

# Garett
garett = Persona("Garett", "19")
garett.saludar()

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__ (nombre, edad)
        self.grado = grado

    def estudiar(self):
        print(f"{self.nombre} está estudiando el grado {self.grado}.")

estudiante1 = Estudiante("Gabriela", 29, "Maestría")
estudiante1.saludar()
estudiante1.estudiar()