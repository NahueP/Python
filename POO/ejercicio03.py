# Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro. Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes. Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica():
    def __init__(self,llantas,color,precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

class Carro(Fabrica):
    def datos(self):
        print("Cantidad de llantas:", self.llantas)
        print("Color:", self.color)
        print("Precio:", self.precio)


class Moto(Fabrica):
    def datos(self):
        print("Cantidad de llantas:", self.llantas)
        print("Color:", self.color)
        print("Precio:", self.precio)


carro = Carro('4','rojo','500000')
moto = Moto('2','negra',"150000")

carro.datos()
moto.datos()
