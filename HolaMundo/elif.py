# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.

palabra1 = input("Ingrese una palabra: ");
palabra2 = input("Ingrese una Otra: ");

if len(palabra1) < 3 or len(palabra2) < 3:
    print("No riman porque una de ellas tiene menos de 3 caracteres")
elif palabra1[-3:] == palabra2[-3:]:
    print("Riman")
elif palabra1[-2:] == palabra2[-2:]:
    print("Riman un poco")
else:
    print("No riman")

