# def funcion():
#     global num1 
#     global num2 
#     num1 = 50
#     num2 = 30
#     resultado = num1+num2
#     print(resultado)


# funcion()

# resultado2 = num1-num2

# print(resultado2)



# ejercicio 1

# lista = []
# num = 0

# def pedir():
#     i = 0
#     while i < 5:
#         num = int(input('Ingrese un numero: '))
#         lista.append(num)
#         i+=1

# def ordenar():
#     lista.sort()
#     pares = []
#     impares = []

#     for i in lista:
#         if i % 2 == 0:
#             pares.append(i)
#         else:
#             impares.append(i)
    
#     print(pares)
#     print(impares)


# pedir()
# ordenar()


# ejercicio 2

num = int(input("Ingrese un numero: "))


def factorial(numero):
    i=1
    f1 = numero
    

    while numero > i:
        
        numero -= 1

        f1 *= numero
       
    print(f1)   

    


factorial(num)