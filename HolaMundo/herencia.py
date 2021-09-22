class Vehiculo():
    def __init__(self, asientos, ruedas):
        self.asientos = asientos
        self.ruedas = ruedas

    def Acelerar(self):
        print("Acelero..")


auto = Vehiculo('2','4')

print('auto tiene {} asientos y {} ruedas'.format(auto.asientos,auto.ruedas))
auto.Acelerar()