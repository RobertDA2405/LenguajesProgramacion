# Ejemplo de encapsulación
class MiClase:
    def __init__(self):
        self.__atributo_privado = 10

    def metodo_publico(self):
        print("Método público")

    def __metodo_privado(self):
        print("Método privado")

objeto = MiClase()
objeto.metodo_publico()      # Salida: "Método público"
objeto.__metodo_privado()    # Esto causará un error, ya que el método es privado