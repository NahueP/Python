# Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    nombre = ""
    nota = 0

    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    


    def calificacion(self):
        if int(self.nota) > 5:
            print("Aprobado")
        else:
            print("Desaprobado")
    


alumno1 = Alumno("Nahuel","10")
alumno2 = Alumno("Josesito","2")


print(alumno1.nombre)
alumno1.calificacion()

print(alumno2.nombre)
alumno2.calificacion()
        