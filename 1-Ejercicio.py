import math
from datetime import datetime


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


#6)Crea un programa que invierta el orden de una cadena de texto sin usar funciones propias del lenguaje que lo hagan de forma automática.
# * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"

#frase = input('Ingresa una palabra o frase: ')
#frase_al_reves = ''
#
#for palabra in range (len(frase)-1,-1,-1):
#    frase_al_reves += frase[palabra]
#print(frase_al_reves)


#7) Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# * Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# * NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# * Ejemplo: Ana lleva al oso la avellana.

def palindromo (palabra):
    #Invierto la cadena con slicing[::-1]
    if palabra == palabra[::-1]:
        print(f'la palabra {palabra} digitada SI es palíndromo')
    else:
        print(f'la palabra {palabra} digitada NO es palíndromo')

def ingreso_palabra ():
    palabra = input('Ingrese una palabra: ')
    palabra = palabra.lower()
    palindromo(palabra)

#ingreso_palabra()


#8)Escribe una función que calcule y retorne el factorial de un número dado de forma recursiva.
def factorial (numero):
    total = 1
    for digito in range (1,numero+1,1):
        total *= digito
    print(f'El factorial de {numero} es = {total}')

def ingreso_numero():
    numero = int(input('Ingrese un número: '))
    factorial(numero)
    
#ingreso_numero()


#9)Escribe una función que calcule si un número dado es un número de Armstrong (o también llamado narcisista).
# * Si no conoces qué es un número de Armstrong, debes buscar información al respecto (Ejm. 153 = 1^3+5^3+3^3 = 1+125+27 = 153)

def numero_armstrong (numero):
    total = 0
    #Convertimos el numero a string luego lo separamos y despues lo convertimos a numeros y lo dejamos en una lista
    numeros_separados = [int(digito) for digito in str(numero)]
    for num in numeros_separados:
        total += math.pow(num, len(numeros_separados))
    total = int(total)
    if total == numero:
        print(f'El número {numero} SI es Armstrong')
    else:
        print(f'El número {numero} NO es Armstrong')
        
def insertar_numero ():
    numero = int(input('Inserte un número: '))
    numero_armstrong(numero)

#insertar_numero()


#10)Crea una función que reciba un String de cualquier tipo y se encargue de poner en mayúscula la primera letra de cada palabra.
# * - No se pueden utilizar operaciones del lenguaje que lo resuelvan directamente.
def letra_mayuscula (cadena):
    #Convierto la cadena de caracteres en lista
    cadena_lista = cadena.split()
    for palabra in range (0,len(cadena_lista),1):
        cadena_lista[palabra] = cadena_lista[palabra][0].capitalize() + cadena_lista[palabra][1:]
    cadena_lista = " ".join(cadena_lista)
    print(cadena_lista)

def pedir_palabra ():
    cadena = input('Ingresa una frase: ')
    letra_mayuscula(cadena)

#pedir_palabra();


#11) Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# * - Los signos de puntuación no forman parte de la palabra.
# * - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# * - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.

#frase = input('Ingrese una frase: ')
#frase = frase.lower()
#frase = frase.split()
#
##Listas de palabras y cuantas hay
#lista_palabras = []
#conteo_palabras = []
#
##Recorremos la frase que ahora es una lista 
#for palabra in frase:
#    #recorremos y verificamos si la palabra esta en lista_palabras y aumentamos su contador de acuerdo al indice en conteno_palabras
#    if palabra in lista_palabras:
#        #Aplicamos la opcion index() para encontrar la palabra en la lista y devuelve su indice posicion donde se encunetra la palabra 
#        indice = lista_palabras.index(palabra)
#        conteo_palabras[indice] += 1
#    else:
#        #Si no esta la plabra la agregamos como nueva y un aumento de la variable
#        lista_palabras.append(palabra)
#        conteo_palabras.append(1)
#
##Recorremos la lista_palabras y conteo de plabras para saber cuantos datos hay en cada uno 
#for repeticion in range (0, len(lista_palabras)):
#    print(f'{lista_palabras[repeticion]} = {conteo_palabras[repeticion]}')


#12) Crea un programa se encargue de transformar un número decimal a binario sin utilizar funciones propias del lenguaje que lo hagan directamente.

#numero = int(input('Ingresa un número decimal: '))
#lista_binario = []
#
#while numero > 0:
#    resul = numero % 2
#    #Agrego el residuo a la lista_binario
#    lista_binario.append(resul)
#    numero //= 2
#lista_binario.reverse()
#
##Muestro de el número de lista (lista_binario) a un numero entero
#num = 0
#for digito in lista_binario:
#    num = num * 10 + digito
#
#print(num)


#13)Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# * - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# * - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
def cadenas_parametros (cadena1, cadena2):
    resul = True
    for caracter1 in cadena1:
        for caracter2 in cadena2:
            if caracter1 == caracter2:
                resul = False
                break
        if not resul:
            break
    if resul == False:
        return f'La cadenas tienen caracteres similares por tal motivo no se pueden mostrar'
    else:
        return f'la cadena 1 tiene estos caracteres "{cadena1}" y las cadena 2 tiene estos otros caracteres "{cadena2}"'
    
def ingreso_cadenas ():
    cadena1 = input('Ingrese la primera cadena de texto: ')
    cadena2 = input('Ingrese la segunda cadena de texto: ')
    cadenas_all = cadenas_parametros(cadena1, cadena2)
    print(cadenas_all)
    
#ingreso_cadenas()


#14) Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# * - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# * - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras " ".
# * - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.

def codigo_morse(cadena):
    alfabeto_morse = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', 
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
    }
    
    # Convertir la cadena a mayúsculas
    cadena = cadena.upper()
    morse = []
    
    for caracter in cadena:
        if caracter in alfabeto_morse:
            morse.append(alfabeto_morse[caracter])
    
    #Convertimos la lista en string con los caracteres de código morse
    return ' '.join(morse)

#print(codigo_morse('Hola mundo'))


#15) Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# * - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# * - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# * - Expresión balanceada: { [ a * ( c + d ) ] - 5 }
# * - Expresión no balanceada: { a * ( c + d ) ] - 5 }

def equilibrio(expresion):
    condiciones = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    lista = []

    for caracter in expresion:
        if caracter in condiciones:
            lista.append(caracter)
        elif caracter in condiciones.values():
            if lista and condiciones[lista[-1]] == caracter:
                lista.pop()
            else:
                return 'La expresión no está equilibrada'
    if not lista:
        return 'La expresión está equilibrada'
    else:
        return 'La expresión no está equilibrada'

#print(equilibrio('{[a*(c+d)]-5}'))
#print(equilibrio('{[a*c+d)]-5}'))


#16)Crea una función que calcule y retorne cuántos días hay entre dos cadenas de texto que representen fechas.
# * - Una cadena de texto que representa una fecha tiene el formato "dd/MM/yyyy".
# * - La función recibirá dos String y retornará un Int.
# * - La diferencia en días será absoluta (no importa el orden de las fechas).
# * - Si una de las dos cadenas de texto no representa una fecha correcta se lanzará una excepción.

def diferencia_dias (string1, string2):
    try:
        string1_for_fecha = datetime.strptime(string1, '%d/%m/%Y')
        string2_for_fecha = datetime.strptime(string2, '%d/%m/%Y')
    except:
        return 'No ingreso las fechas en el formato correcto vuelva a intentarlo'

    resta = (string1_for_fecha - string2_for_fecha).days
    return f'La diferencia de dias entre {string1_for_fecha.date()} y {string2_for_fecha.date()} es de {int(abs(resta))} dias'

def ingreso_fechas ():
    string1 = input('Ingrese la primera fecha bajo el siguiente formato "dd/MM/yyyy": ')
    string2 = input('Ingrese la segunda fecha bajo el siguiente formato "dd/MM/yyyy": ')
    fechas_ingresadas = diferencia_dias (string1, string2)
    return fechas_ingresadas

#print(ingreso_fechas())