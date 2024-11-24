#1)Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
    #* - Múltiplos de 3 por la palabra "fizz".
    #* - Múltiplos de 5 por la palabra "buzz".
    #* - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".

for numero in range(1,101,1):
    if (numero % 3 == 0) & (numero % 5 == 0):
        numero = "fizzbuzz"
    elif numero % 3 == 0:
        numero = "fizz"
    elif numero % 5 == 0:
        numero = "buzz"
    #print(numero)


#2)Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
    #* - La serie Fibonacci se compone por una sucesión de números en
    #* la que el siguiente siempre es la suma de los dos anteriores.
    #* 0, 1, 1, 2, 3, 5, 8, 13...

numero1 = 0
numero2 = 1
for condicion in range(1,51,1):
    #print(numero1)
    resultado = numero1 + numero2
    numero1 = numero2
    numero2 = resultado


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


#4)Escribe una función que reciba dos palabras (String) y retorne verdadero o falso (Bool) según sean o no anagramas.
# * - Un Anagrama consiste en formar una palabra reordenando TODAS las letras de otra palabra inicial.
# * - NO hace falta comprobar que ambas palabras existan.
# * - Dos palabras exactamente iguales no son anagrama.

def anagramas (palabra1, palabra2):
    #Convierto las palabras a minusculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    if palabra1 == palabra2:
        print(f'Las palabras son iguales por tal motivo no son anagramas')
    else:
        #Usando la funcion sorted para determinar que las palabras sean igual de largas
        if sorted(palabra1) == sorted(palabra2):
            print (f'Las palabras {palabra1} y {palabra2} SI son anagramas')
        else:
            print (f'La palabras {palabra1} y {palabra2} NO son anagramas')

def ingreso_palabras ():
    palabra1 = input("Ingresa una palabra: ")
    palabra2 = input("Ingresa otra palabra: ")
    anagramas(palabra1, palabra2)

##ingreso_palabras()


#5)Crea una única función (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# * - La función recibirá por parámetro sólo UN polígono a la vez.
# * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# * - Imprime el cálculo del área de un polígono de cada tipo.

def area_poligono (opcion):
    if opcion == 1:
        base = int(input('Ingrese la base del triángulo: '))
        altura = int(input('Ingrese la altura del triángulo: '))
        print(f'El área del triángulo es: {(base * altura) / 2}')
    elif opcion == 2:
        lado = int(input('Ingrese un lado del cuadrado: '))
        print(f'El área del cuadrado es: {lado**2}')
    elif opcion == 3:
        base = int(input('Ingrese la base del rectángulo: '))
        altura = int(input('Ingrese la altura del rectángulo: '))
        print(f'El área del rectangulo es: {base * altura}')
    else:
        print('Ups. La opción que selecciono no esta en los parametros del programa vuelva a reiniciar y eligir otra opción valida.')

def ingreso_opcion ():
    opcion = int(input('El siguiente programa puede calcular el área de tres polígonos, a continuación elige una opcion para el cual calcular su area: \n1 - Triángulo. \n2 - Cuadrado. \n3 - Rectángulo. \nIngresa aqui tu elección: '))
    area_poligono(opcion)

#ingreso_opcion()
