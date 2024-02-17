class Student:
    def __init__(self, id, name, career):
        self.id = id
        self.name = name
        self.career = career

    def __str__(self):
        return f"Nombre: {self.name}\nCarrera: {self.career}"