#1)Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
    #* - Múltiplos de 3 por la palabra "fizz".
    #* - Múltiplos de 5 por la palabra "buzz".
    #* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

#for numero in range(1,101,1):
#    if (numero % 3 == 0) & (numero % 5 == 0):
#        numero = "fizzbuzz"
#    elif numero % 3 == 0:
#        numero = "fizz"
#    elif numero % 5 == 0:
#        numero = "buzz"
#    print(numero)


#2)Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
    #* - La serie Fibonacci se compone por una sucesión de números en
    #* la que el siguiente siempre es la suma de los dos anteriores.
    #* 0, 1, 1, 2, 3, 5, 8, 13...

#numero1 = 0
#numero2 = 1
#for condicion in range(1,51,1):
#    print(numero1)
#    resultado = numero1 + numero2
#    numero1 = numero2
#    numero2 = resultado


#3)Escribe un programa que se encargue de comprobar si un número es o no primo.

#numero = int(input("Ingrese el número: "))
#constante = 0
#if numero <= 1:
#    print("Los numeros menores a 1 no son primos")
#else:
#    for condicion in range(2,numero+1,1):
#        if numero % condicion == 0:
#            constante += 1
#    if constante == 1:
#        print(f"El número {numero} es primo")
#    else:
#        print(f"El número {numero} no es primo")
## * Hecho esto, imprime los números primos entre 1 y 100.
#for variable in range(2,101,1):
#    primo = True
#    for variable2 in range(2,variable,1):
#        if variable % variable2 == 0:
#            primo = False
#        break
#    if primo == True:
#        print(variable)

