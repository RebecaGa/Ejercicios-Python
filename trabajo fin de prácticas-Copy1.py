#!/usr/bin/env python
# coding: utf-8

# In[2]:


#EJERCICIO 1. COMPARACION DE NÚMEROS

print ("Vamos a comparar dos números")
num1 = float(input("Escriba un número "))
num2 = float(input("Ahora escriba otro "))
if num1 > num2:
    print("El primer número es MAYOR que el segundo")
elif num1 < num2:
    print("El primer número es MENOR que el segundo")
else:
    print("Son iguales")
print("¿Lo volvemos a intentar")    


# In[3]:


#EJERCICIO 2.DETERMINAR QUÉ NÚMERO ES MAYOR O MENOR O SI SON IGUALES
def main():
    print("Ahora le voy a indicar qué número es el mayor")

    num1 = int(input("Escriba un número positivo "))
    if num1 < 0:
        print("Por favor, escriba un número mayor que cero")
        print("Inténtelo de nuevo")
    elif num1 >= 0:
        num2 = int(input("Escriba otro número "))
    if num2 < 0:
        print("Por favor, intentamos comparar número positivos, por favor, escriba un número mayor que 0")
        print("Inténtelo de nuevo")
    elif num1 > num2:
        print("el número mayor es ") 
        print(num1)
        print("el número menor es ")
        print(num2)
    elif num1 < num2:
        print("el número mayor es ")
        print(num2)
        print ("el número menor es ")
        print (num1)
    else:
        print("Son iguales")
    print("¿Lo volvemos a intentar?")
        
if __name__ == "__main__":
    main()


# In[4]:


#EJERCICIO 3. MOSTRAR LOS CUADRADOS
print("MOSTRAMOS LOS CUADRADOS DEL 1 AL 100")
for i in range(101):
    print(f"cuadrado de {i} es {i ** 2}")


# In[5]:


#EJERCICIO 4. LISTAR NÚMEROS PARES

def main():
    print("Determinar los pares comprendidos entre dos números")
    inicial = int(input("Escriba el número entero inicial: "))
    final = int(input("Escriba el número entero final: "))
    print("La lista es :")
    if inicial < final:
        print(list(range(inicial, final +1)))
    else:
        print(list(range(final, inicial +1)))
   

    print("Los pares son: ")
    if final < inicial:
        if inicial % 2 != 0:
            print(list(range(final +1, inicial +1, 2)))
        else:
            print(list(range(final, inicial +1, 2)))
    elif inicial % 2 != 0:
        print(list(range(inicial + 1, final + 1, 2)))
    else:
        print(list(range(inicial, final + 1, 2)))


if __name__ == "__main__":
    main()
    
print()
print("¿Lo intentamos otra vez?")


# In[6]:


#EJERCICCIO 5 Media de una serie de números

#Solicitar al usuario que introduzca números hasta que se llegue a introducir uno negativo, 
#lo cual interrumpirá las peticiones. Mostrar en pantalla la suma y 
#la media de los números positivos introducidos. Indicar cuántos valores introducidos son superiores a la media.


numeros = []

def media():
    a = int(input("Escriba un número mayor que 0: "))
    while a > 0:
        numeros.append(a)
        a = int(input("Escriba un número mayor que 0: "))
    if a <= 0:
        print("Vamos a calcular la media de {}".format(numeros))
        suma = sum(numeros)
        total = len(numeros)
        media2 = suma/total
        print("la suma es {}".format(suma))
        print("la media es {}".format(media2))
        

media()


# In[1]:


#EJERCICIO 6 Calculadora

#Pedir al usuario dos números válidos, si no son válidos seguir pidiendo valores. 
#Efectuar con ellos la suma, resta, multiplicación, división, división entera, resto, y potencias. 
#Utilice control de errores para evitar el error de división entre cero.

def calculadora():
    lista = ["yes", "y", "si", "Sí", "s", "S", "sí", "Si"]
    while True:
        a = input("Escriba un número ")
        b = input("Escriba un número ")
        try:
            a = float(a)
            b = float(b)
            print("Vamos a realizar calculos con {} y {}".format(a, b))
            try:
                suma = a + b
                print("La suma es {} ".format(suma))
                resta = a - b
                print("La resta es {} ".format(resta))
                multi = a*b
                print("La multiplicación es {} ".format(multi))
                pot = a**b
                print("{} elevado a {} es {}".format(a, b, pot))
                div = a/b
                print("La división es {} ".format(div))
            except ZeroDivisionError:
                print("Divisor 0")
            try:
                divi = a//b
                print("La división entera es {}".format(divi))
            except ZeroDivisionError:
                print("Divisor 0")
            try:
                resto = a%b
                print("El resto es {} ".format(resto))
            except ZeroDivisionError:
                print("Divisor 0")
            confirm = input("¿Quieres seguir? ")
            
            if confirm in lista:
                pass
            else:
                print("Me ha gustado jugar contigo. Hasta pronto")
                break
        except ValueError:
            print("La entrada es incorrecta: escriba números")
        
                
            
            
calculadora()


# In[2]:


# EJERCICIO 7. Divisores de un número
#Generar un número aleatorio entre 2 y 1.000 mostrando en pantalla todos sus divisores

import random
a = random.randint(2, 1000)

def Divisores():
    a = random.randint(2, 1000)
    print("El número seleccionado es: {}".format(a))

    print(f"Los divisores de {a} son ", end="")
    for i in range(1, a + 1):
        if a % i == 0:
            print(i, end=" ")


Divisores()


# In[3]:


#EJERCICIO 8 Comparar medias de aleatorios
# Generar 12 números aleatorios entre 0 y 100 y calcular su media. 
# Generar otros 12 números aleatorios entre 0 y 100 y calcular su media. 
# Finalmente muestre en pantalla las medias de ambas series y diga cuál de las dos ha resultado mayor. Utilice funciones.

import random
from random import randint
lista = []


def Compara():
    for x in range(12):
        a = randint(0,100)
        lista.append(a)

    print("Esta es la primera lista: {}".format(lista))


    numeros = [random.randint(1,100) for i in range(12)]
    print("Esta es la segunda lista: {}".format(numeros))


    s = sum(lista)
    l = len(lista)
    media1 = s/l
    print("La media de la primera lista es {}".format(media1))


    s1 = sum(numeros)
    l1 = len(numeros)
    media2 = s1/l1
    print("La media de la segunda lista es {}".format(media2))

    if (media1 > media2):
        print("La media de la PRIMERA lista es mayor")
    elif (media1 == media2):
        print("Las medias son IGUALES")
    else:
        print("La media de la SEGUNDA lista es mayor")

Compara()


# In[4]:


#EJERCICIO 9. Tablas de multiplicar hasta 12×12
# Generar y mostrar en pantalla todas las tablas de multiplicar desde la tabla del 1 hasta la tabla del 12. 
# El último valor que se multiplicará será 12 × 12 = 144.

tabla_desde = 1 
tabla_hasta = 12 
desde = 1
hasta = 12 

for i in range(tabla_desde, tabla_hasta + 1):
    print(f'Tabla de multiplicar del {i}:') 
    for x in range(desde, hasta + 1):
        print(f'{i} x {x} = {i * x}')
    print() 


# In[3]:


#EJERCICIO 10.Frecuencia de caracteres
#Pedir al usuario que escriba un párrafo de texto. Mostrar en pantalla cuantas veces aparece cada letra del alfabeto.

from collections import Counter
import string



def texto():
    tex = input("Por favor introduzca un texto: ")
    texto = tex.replace(" ","").replace("á", "a").replace('é','e').replace('í','i').replace('ó','o').replace('ú','u')
    text = texto.lower()
    
    a = Counter(text)
    a = sorted(a.items())
    print((a))
    
texto()     


# In[2]:


#EJERCICIO 11.Calculadora de IVA
#Programar dos casos para el cálculo del IVA (Impuesto sobre el Valor Añadido). 
#El caso A calcula el precio con IVA dados el precio base y el porcentaje de IVA. 
#El caso B calcula el precio base dados el precio con IVA y el porcentaje de IVA. 
#Utilice funciones. Establezca un menú donde el usuario pueda elegir que caso desea resolver.

def opcionA():
    base = input("Introduzca la base imponible ")
    iva = input("Introduzca el porcentaje de IVA, sin signos de puntuación ")
    if iva < '0':
        print("Por favor, el IVA tiene que ser positivo")
    else:
        try:
            bas = float(base)
            iv = float(iva)
            print("Vamos a calcular el precio: ")
            i = bas * iv
            c = 100
            iva1 = i/100
            precio = iva1 + bas
            print(precio)
        except ValueError:
                print("Lo lamento, el valor introducido no es válido. Vuelvalo a intentar")
                
           
        
        
def opcionB():
    pre = input("Introduzca el precio ")
    iva = input("Introduzca el porcentaje de IVA, sin signos de puntuación ")
    if iva < '0':
        print("Por favor, el IVA tiene que ser positivo")
    else:
        try:
            base = float(pre)
            iv = float(iva)
            print("Vamos a calcular la base imponible: ")
            c = 100
            a = (iv/c)+1
            bas = base / a
            print(bas)
        except ValueError:
                print("Lo lamento, el valor introducido no es válido. Vuelvalo a intentar")

    
    
    
def calculo():   
    op = input("""¿Qué desea conocer? 
            Opción A = Usted conoce la base imponible y el IVA, y desea conocer el PRECIO
            Opción B = Usted conoce el precio total y el IVA aplicado, pero desea conocer la BASE IMPONIBLE """)
    lista = ["A", "a"]
    lista2 = ['B', 'b']
    if op in lista:
        opcionA()
    elif op in lista2:
        opcionB()
    else:
        print("Introduzca A o B")
    c = input("¿Desea realizar otro calculo?")
    lista = ['s', 'si', 'sí', 'Si', 'SI', 'Sí']
    if c in lista:
        calculo()
    else:
        print("¡Hasta Pronto!")
    

    
calculo()


# In[7]:


#EJERCICIO 12. Edad
#Establezca un procedimiento en el que el código toma la fecha del sistema e indicando 
#su fecha de nacimiento le diga cuántos años tiene y 
#cuantos días faltan para que llegue su próximo cumpleaños

import datetime
from datetime import date

year = int(input('Introduzca su año de nacimiento: '))
month = int(input('Introduzca su mes de nacimiento: '))
day = int(input('Introduzca su día de nacimiento: '))
date1 = datetime.date(year, month, day)

print("Su fecha de nacimiento es: {}".format(date1))

def edad(naci):
    hoy = datetime.date.today()
    if hoy < naci:
        print('error en la fecha de nacimiento')
    else:
        ano = naci.year
        mes = naci.month
        dia = naci.day
 
        fecha = naci
        edad = 0
        while fecha < hoy:
            edad += 1
            fecha = datetime.date(ano+edad, mes, dia)
 
        print('Su edad es: %s años' % (edad-1))
    

def hastacumple():
    hoy = date.today()
    cumpleaños = date(hoy.year, month, day)

    if cumpleaños < hoy:
            cumpleaños = cumpleaños.replace(year=hoy.year + 1)
    cumpleaños
    hastacumple = abs(cumpleaños - hoy)
    print("Te quedan {} días hasta tu próximo cumpleaños".format(hastacumple.days))
 
edad(date1)
hastacumple()


# In[8]:


#EJERCICIO 13.Comprobar si un número es primo
#Genere e imprimir una lista con los mil primeros números primos, 
#luego genere un número aleatorio entero entre 2 y 7.919. 
#Muestre en pantalla el número aleatorio e indique si pertenece a la lista de los mil primeros números primos.

import math
 
t = int(input('Cuántos primos quieres?: '))
p = 1   #contador de primos encontrados
c = 3   #se evalúan desde 3 en adelante
r = [2] #cadena con el primer resulatdo listo
while p < t:
    fact1 = math.factorial(c-1)
    if fact1 % c == c-1:
        float(c)
        r.append(c)
        p += 1  #se ha encontrado otro primo
    c += 1      #probar con siguiente entero
print(r)        #mostrar resultados almacenados en r


import random
a = random.randint(2, 7919)
print(a)

def esta():
    a = random.randint(2, 7919)
    print("El número aleatorio es {}".format(a))
    if a in r:
        print("El número {} se encuentra en la lista de primos".format(a))
    else:
        print("El número {} no se encuentra en la lista de primos".format(a))
        
esta()
   


# In[9]:


#EJERCICIO 14.Números aleatorios con y sin repetición
#Generar dos listas de 10 elementos cada una, con números enteros, aleatorios, entre 1 y 20, 
#donde en una de ellas se pueden llegar a repetir y en la otra no se admiten repeticiones. 
#Generar una tercera lista con todos los elementos que se repitan en ellas, 
#pero no debe repetirse ningún elemento en la nueva lista.

from random import sample

lista1 = sample([x for x in range(1,20)],10)
print("La primera lista que hemos generado es: {}".format(lista1))

lista2 = []

for i in range(10):
    a = random.randint(1,20)
    lista2.append(a)
print("La segunda lista que hemos generado es: {}".format(lista2))

lista3 = []

for i in lista1:
    if i in lista2:
        lista3.append(i)
print("La nueva lista generada es {} ".format(lista3))    


# In[10]:


#EJERCICIO 15.Ordenar una lista
#Generar una lista de números aleatorios. Ordenar la lista sin usar sort.

from random import sample

lista = sample([x for x in range(1,20)],10)
print("La lista a ordenar es {}".format(lista))

def ordenar_max(lista):
  for xd in range(len(lista)):
    for m in range(len(lista)):
      if lista[xd] > lista[m]:
        tmp = lista[xd]
        lista[xd] = lista[m]
        lista[m] = tmp
  
  print("Lista ordenada", end=": ")
  for lt in range(len(lista)):
    print(lista[lt], end=":")
  
        
def ordenar_min(lista):
  for xd in range(len(lista)):
    for m in range(len(lista)):
      if lista[xd] < lista[m]:
        tmp = lista[m]
        lista[m] = lista[xd]
        lista[xd] = tmp
  
  print("Lista ordenada", end=": ")
  for lt in range(len(lista)):
    print(lista[lt], end=":")
  
print("""
\nSelecciona una de las siguientes opciones

1) Ordenar de mayor a menor
2) Ordenar de menor a mayor

""")
selec = int(input("Selecciona una opción: "))
if selec == 1:
  ordenar_max(lista)
elif selec == 2:
  ordenar_min(lista)


# In[11]:


#EJERCICIO 16.Función separa
#Generar una lista de 15 elementos, con números enteros, aleatorios, entre -20 y 20. 
#Cree una función que separe los elementos de la lista anterior en dos listas, por un lado, 
#los números pares y por otro, los impares. Las nuevas listas tendrán sus elementos ordenados y sin repetición. 
#Indique en cuál de las dos listas la suma de sus elementos es mayor.

listap = []
for i in range(15):
    a = random.randint(-20, 20)
    listap.append(a)
print("La lista que hemos generado es: {}".format(listap))


def separa():
    par = []
    impar = []
    for i in listap:
        if i not in par:
            if i % 2 == 0:
                par.append(i)
            else:
                if i not in impar:
                    impar.append(i)
    
    print("La lista par es: {}".format(sorted(par)))
    print("La lista impar es : {}".format(sorted(impar)))
    a = sum(par)
    print("La suma de la lista par es {}".format(a))
    b = sum(impar)
    print("La suma de la lista impar es {}".format(b))
    if a < b:
        print("""
                La suma de la lista IMPAR es mayor""")
    else:
        print("""
                La suma de la lista PAR es mayor""")
    
            
separa()


# In[13]:


#EJERCICIO 17.Binario a decimal
#Pedir al usuario que introduzca un número binario y convertirlo a decimal. 
#Mostrar en pantalla también el modo de llegar a ese resultado. 
#Por ejemplo, si el binario es 101011, entonces se ha de imprimir 
#el proceso que es: 1*2^5 + 0*2^4 + 1*2^3 + 0*2^2 + 1*2^1 + 1*2^0 = 43


numero_binario = input("Introduce un número binario ")

for digito_string in numero_binario:
    digito = int(digito_string)
    print(digito)
    
posicion = len(numero_binario) - 1 #posición del primer dígito por la izquierda
  
for posicion, digito_string in enumerate(numero_binario[::-1]):
    digito = int(digito_string)
    print(f'Dígito: {digito}, posición: {posicion}')
    
for posicion, digito_string in enumerate(numero_binario[::-1]):
    digito = int(digito_string)
    multiplicacion = digito * 2 ** posicion;
    print(f'Dígito: {digito}, posición: {posicion}, multiplicación: {multiplicacion}')
    
numero_decimal = 0 #aquí iremos sumando el resultado de cada multiplicación

for posicion, digito_string in enumerate(numero_binario[::-1]):
    numero_decimal += int(digito_string) * 2 ** posicion

print(f'El número decimal que buscamos es {numero_decimal}')


# In[1]:


#EJERCICIO 18.Decimal a binario
#Pedir al usuario que introduzca un número decimal y convertirlo a binario. 
#Mostrar en pantalla también el modo de llegar a ese resultado. Como ejemplo se puede ver la siguiente imagen.

def binarizar(decimal):
    binario = ''
    while decimal // 2 != 0:
        binario = str(decimal % 2) + binario
        decimal = decimal // 2
    return str(decimal) + binario

numero = int(input('Introduce el número a convertir a binario: '))
print(binarizar(numero))


# In[4]:


#EJERCICIO 19.Suma de dos números para llegar al target
#Generar un número entero aleatorio entre 2 y 20. 
#A este número le llamaremos target. 
#Generar una lista de números enteros entre -10 y 10. 
#La lista puede tener desde un mínimo de dos elementos a un máximo de 6. 
#La lista debe contener dos números que sumados nos den el target. 
#El programa generará un target y una lista y verificará que se cumple la condición de la suma. 
#En caso de que no se cumpla seguirá generando otro target y otra lista hasta conseguirlo. 
#La solución debe ser única. Solo puede haber un par de números que sumados den el target. 
#Como ejemplo se puede ver la siguiente imagen donde mostramos tres listas que cumplen la condición. 
#En su caso, debe generar y mostrar cien listas que cumplan los requisitos pedidos.

import random

num = 1

while num < 101:

    
    t = random.randint(2,20) #t de target para abreviar
    t = str(t)
    
    
    listap = []
    for i in range(2):
        a = random.randint(-10, 10)
        listap.append(a)
        b = sum(listap)
        b = str(b)
    if b == t:
        print("LISTA NÚMERO: {}".format(num))
        print('El TARGET es: {}'.format(t))
        print("La lista es: {}".format(listap))
        print("La suma es: {}".format(b))
            
        num += 1
        print("""ESTA LISTA REÚNE LOS REQUISITOS
        """)
            
        
    
    while (b != t):
        c = random.randint(-10, 10)
        listap.append(c)
        d = sum(listap)
        d = str(d)
        
        if d == t:
            print("LISTA NÚMERO: {}".format(num))
            print('El TARGET es: {}'.format(t))
            print("La lista es: {}".format(listap))
            print("La suma es: {}".format(d))
            
            num += 1
            print("""ESTA LISTA REÚNE LOS REQUISITOS
            """)
            break
        if len(listap) == 6:
            break
   


# In[2]:


#EJERCICIO 20.Segundo mínimo en listas anidadas
#Disponemos de la siguiente lista anidada [["Ana",1],["Raul",1],["Jose",9],["David",7],["Eva",8],["Felipe",4],["Héctor",9],["Isabel",4],["Susana",5]]. 
#Estamos buscando los nombres que están asociados al segundo mínimo. 
#Para esta lista, el procedimiento debería proporcionar como salida: Felipe, Isabel. 
#Crear un procedimiento que genere listas anidadas similares a la del ejemplo, de longitud variable y 
#que garanticen que existe el segundo mínimo. 
#El programa mostrará en pantalla la lista generada y el nombre o nombres asociados con el segundo mínimo. 
#Utilizar funciones.

lista = [["Ana",1],["Raul",1],["Jose",9],["David",7],["Eva",8],["Felipe",4],["Héctor",9],["Isabel",4],["Susana",5]]
print(lista)


# In[1]:


#EJERCICIO 21. Lista de impares
#Generar números enteros aleatorios entre 10 y 99 (ambos incluidos) que se incorporen a una lista de longitud 17. 
#Generar continuamente listas de este tipo hasta lograr una donde todos sus elementos sean impares y sin repetición. 
#Imprimir la lista obtenida de forma ordenada de mayor a menor. 
#Imprimir el tiempo que se ha tardado en lograr esa lista expresado en segundos con hasta 6 decimales

import random 
from time import time

inicial = time()   
b = []
d = 17
a = 0
while len(b) != 17:
    a = random.randint(10, 99)
    if a % 2 != 0:
        if not a in b:
            b.append(a)
    if len(b) == 17:
        break
        
print("La lista que hemos generado es {}".format(sorted(b))) 

final = time()
tiempo = final - inicial
print("Tiempo de ejecución: {0:.10f} segundos".format(tiempo))


# In[ ]:


#EJERCICIO 22.El objeto persona
#Crear la clase Persona con los atributos nombre, edad, profesión, altura, ciudad y otro de su elección. 
#Crear un par de objetos Persona. Finalmente deseamos preguntar a cada persona su edad y su ciudad

class Persona():
    """Clase que representa una Persona"""

    def __init__(self, nombre, edad, prof, alt, ciudad, sexo):
        """Constructor de clase Persona"""
        self.nombre = nombre
        self.edad = edad
        self.prof = prof
        self.alt = alt
        self.ciudad = ciudad
        self.sexo = sexo
        
    def saludar(self):
        print("Hola me llamo {} y tengo {} años y vivo en {}".format(self.nombre, self.edad, self.ciudad))
        
    def preguntar(self):
        print("Hola, ¿Cómo te llamas y cuántos años tienes? ¿Podrías decirme donde vives?")
        
        

Ana = Persona("Ana", 23, "Profe", 1.67, "Madrid", "F")
Juan = Persona("Juan", 32, "Butanero", 1.90, "Sevilla", "M")

Ana.preguntar()
Ana.saludar()
Juan.preguntar()
Juan.saludar()


# In[1]:


#EJERCICIO 23.El objeto auto
#Crear la clase Car y dotarla de una serie de atributos y métodos. 
#Crear tres o más automóviles y ordenarlos por su velocidad máxima que son capaces de alcanzar. 
#Verificar los que están aparcados o circulando.

from operator import attrgetter

class Car():
    
    def __init__(self, marca, modelo, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = velocidad
        self.arrancado = False
        
    def mostrar1(self):
        print(self.modelo, self.marca, self.velocidad)
        
        
    
    def mostrar(self):
        print ("El modelo del coche es:", self.modelo, "\nSu marca es:", self.marca,"\ny alcanza una velocidad de ", self.velocidad, "por hora") 

        
    def estado(self, aparcado):
        self.aparcado = aparcado
        if (self.aparcado == False):
            print("Este coche está aparcado")
        else:
            print("Este coche está circulando")
            
    
listaCoches = []        
            
Coche1 = Car("Renault", "Twingo", 120)
Coche2 = Car("Peugeot", "5008", 160)
Coche3 = Car("Fiat", "Panda", 100)
Coche4 = Car("Mercedes", "Clase A", 180)
Coche5 = Car("Audi", "A3", 200)

listaCoches.append(Coche1)
listaCoches.append(Coche2)
listaCoches.append(Coche3)
listaCoches.append(Coche4)
listaCoches.append(Coche5)

NuevaLista = sorted(listaCoches, key=attrgetter('velocidad'))

for i in range(5):
    NuevaLista[i].mostrar1()
    
print("")   
print("")
Coche1.mostrar()    
print(Coche1.estado(False))

print("")   
print("")
Coche2.mostrar()    
print(Coche2.estado(True))  

print("")   
print("")
Coche3.mostrar()    
print(Coche3.estado(True)) 

print("")   
print("")
Coche4.mostrar()    
print(Coche4.estado(False)) 


# In[1]:


#EJERCCICIO 24.Objetos geométricos
#Crear la clase Rectángulo con los atributos ancho, largo. 
#Incluir en el método constructor los argumentos ancho y largo. 
#Crear un método para calcular el área del rectángulo y otro para calcular su perímetro. 
#Crear la clase Circulo con el atributo radio. 
#Incluir en el método constructor el argumento radio. 
#Crear un método para calcular el área del círculo y otro para calcular su perímetro. 
#Para usar PI utilice math.pi. 
#Crear dos objetos del tipo rectángulo y otros dos objetos del tipo circulo, 
#proporcione valores aleatorios a sus parámetros y calcule sus superficies y perímetros redondeando a dos decimales.

import math

class Rectangulo():
    
    def __init__ (self, ancho, largo):
        self.ancho = ancho
        self.largo = largo
        
    def Area(self):
        self.area = self.ancho * self.largo
        print("El área del rectangulo es",self.area,"cm")
        
    def Peri(self):
        self.peri = 2*(self.ancho + self.largo)
        print("El perímetro del rectangulo es", self.peri,"cm")
        
class Circulo():
    
    def __init__(self, radio):
        self.radio = radio
        
    def ArCir(self):
        self.arcir = self.radio * (math.pi**2)
        print("El área del círculo es",round(self.arcir,2),"cm")
    
    def PerCir(self):
        self.percir = 2*self.radio*math.pi
        print('El perímetro del círculo es',round(self.percir,2),'cm')
    
        
R1 = Rectangulo(2,4)
R2 = Rectangulo(3,6)
R1.Area()
R1.Peri()

C1 = Circulo(1)
C2 = Circulo(3)
C1.ArCir()
C1.PerCir()


# In[21]:


#EJERCICIO 25. Capitalización compuesta
#Dado un capital inicial de 100.000 € y un tipo de interés del 6% anual calcular 
#cómo evoluciona el capital durante una serie de años hasta el plazo que nos indique el usuario. 
#Si el usuario, cuando se le pregunte, no indica plazo y pulsa Enter, tomar como plazo por defecto 10 años.
#Junto a cada capital indicar también los intereses devengados cada año. 
#Mostrar en pantalla los importes redondeados a dos decimales y 
#conseguir que las dos columnas queden alineadas al punto decimal.  
#Mostrar un gráfico que ilustre la evolución del capital a lo largo del tiempo.


ci = 100000
cp = []
años = []
i = 0.06
n = 0
m = 0

def calculo():
    while True:
        try:
            plazos = int(input("Introduce el plazo de tu inversión: "))
            print("Tu inversión inicial es 100.000 €")
            if plazos > 0:
                for p in range(plazos):
                    n = p+1
                    años.append(n)
                    cf = ci*(1+i)**n
                    cp.append(cf)
                    ia = cf - ci
                    if p < 1:
                        inter = ci * i
                    else:
                        inter = cp[p-1] * i
                    
                    print("CAPITAL año {:2d}: {} €  \t INTERESES generados año {:2d}:  {:>10.2f} €    \t intereses ACUMULADOS: {:>10.2f} € ".format(n,round(cf,), n,round(inter,2),round(ia,2)))
                
                break
               
            else:
                print("por favor, introduzca un número positivo")
            
        except ValueError:
            print("El plazo de inversión por defecto es 10 años")
            print("Tu inversión inicial es 100.000 €")
            for m in range(10):
                n = m+1
                cf = ci*(1+i)**n
                años.append(n)
                cp.append(cf)
                ia = cf - ci
                if m < 1:
                    inter = ci * i
                else:
                    inter = cp[m-1] * i
                
                print("CAPITAL año {:2d}: {} €  \t INTERESES generados año {:2d}:  {:>10.2f} €    \t intereses ACUMULADOS: {:>10.2f} € ".format(m+1,round(cf,), m+1,round(inter,2),round(ia,2)))
                
            break
        
    
calculo()

get_ipython().run_line_magic('matplotlib', 'notebook')
import matplotlib.pyplot as plt

plt.plot([años],[cp],'bs')
plt.show()


# In[ ]:


#EJERCICIO 26.Generar palabras
#Generar palabras de 6 caracteres del tipo cvcvcv, 
#donde c representa una consonante y donde v representa una vocal.
#Hacer una lista de varias palabras separadas por coma, y probar 
#la lista en una página de dominios de internet para ver si existe alguno de estos libre. Ejemplo: casato.com

import random

char = "bcdfghjklmnñpqrstvwyz"
vocales = "aeiou"
lista = []


def genera():
        a = 1
        while a < 6:
            a = a+2
            con = random.choice(char)
            lista.append(con)
            voc = random.choice(vocales)
            lista.append(voc)
            
        print(lista)
        lista2 = ' '.join(lista)
        print(lista2)    

genera()   

