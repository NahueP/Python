Lista = ['Tomate','Cebolla','Huevos','Leche','Arroz'];

Lista2 = [20, 50, "Curso", 'Python', 3.14]

Lista3 = [1,2,3,4,5,6,7,8,9,10]

Lista4 = ('Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre')

Lista5 = {"Guatemala": "Ciudad de Guatemala", "El Salvador": "San Salvador", "Honduras": "Honduras","Nicaragua": "Managua", "Costa Rica": "San Jose", "Panama": "Panama", "Argentina": "Buenos Aires", "Colombia": "Bogota", "Venezuela": "Caracas", "España": "Madrid"}

# print(Lista2)

# Lista2[0] = input("Ingrese elemento: ")
# Lista2[1] = input("Ingrese otro elemento: ")

# print(Lista2)

# print(Lista3)

# Lista3[4] *= 2
# Lista3[7] *= 2
# Lista3[9] *= 2

# print(Lista3)

# mes = int(input('Ingrese un numero de mes: ')) - 1


# print(Lista4[mes])

pais = input("Ingrese un pais: ")

# pais = pais.lower()
# pais = pais[0].upper() + pais[1:len(pais)]

pais = pais.capitalize()

if(pais in Lista5):
    print("La capital de",pais,"es",Lista5[pais])
else:
    print("No se encuentra el pais")

