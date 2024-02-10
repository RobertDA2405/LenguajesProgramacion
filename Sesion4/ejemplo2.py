class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__ (nombre, edad)
        self.grado = grade

    def estudiar(self):
        print(f"{self.nombre} está estudiando el grado {self.grado}.")

estudiante1 = Estudiante("Gabriela", 29, "Maestría")
estudiante1.saludar()
estudiante1.estudiar()