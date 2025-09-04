#miguel Ramos
#Solución del taller de práctica del curso programacion orientada a objetos.

#imprime un mensaje en la consola
def msj_consola():
    print("Hola, ya se imprimir mensajes en la consola")

#Programa que imprime por pantalla la suma de 1234 y 532.
def suma_numeros():
    a=1234 
    b=532
    c=a+b
    print(f"La suma de {a} y {b} es {c}")

#Programa que imprime por pantalla los números del 1 al 10 000.
def imprimir_numeros():
    inicio=1
    fin=10000
    print("Los números del 1 al 10 000 son: ")
    for i in range(inicio, fin+1):
        print(i)

#Programa que imprime por pantalla los cuadrados de los 30 primeros números naturales.
def imprimir_cuadrados():
    x=30
    print(f"Los cuadrados de los {x} primeros números naturales son: ")
    for i in range(1, x+1):
        print(f"El cuadrado de {i} es {i ** 2}")

#Programa que multiplica los 20 primeros número naturales.
def multiplicar_numeros_consecutivos():
    x=20
    resultado=1
    for i in range(1, x+1):
        resultado *= i
    print(f"La multiplicación de los {x} primeros números naturales es: {resultado}")

#Programa que calcula el área de un rectángulo de los cuales pedimos su alto y ancho (números decimales).
def calcular_area_rectangulo():
    print("Cálculo del área de un rectángulo")
    altura=float(input("Ingrese la altura del rectángulo: "))
    ancho=float(input("Ingrese el ancho del rectángulo: "))
    area=altura*ancho
    print(f"El área del rectángulo es: {round(area, 2)}")

#Programa que lee temperaturas en grados fahrenheit y los convierte a grados centígrados.
def convertir_temperatura():
    temp_far=float(input("CONVERTIDOR DE GRADOS FAHRENHEIT A CENTÍGRADOS\n\nIngrese la temperatura en grados fahrenheit: "))
    temp_cent=(temp_far-32)*5/9
    print(f"{temp_far} grados Fahrenheit en grados centígrados son: {round(temp_cent, 2)} °C")

#msj_consola()
#suma_numeros()
#imprimir_numeros()
#imprimir_cuadrados()
#multiplicar_numeros_consecutivos()
#calcular_area_rectangulo()
convertir_temperatura()