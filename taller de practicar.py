#miguel Ramos
#Solución del taller de práctica del curso programacion orientada a objetos.

#imprime un mensaje en la consola
print("Hola, ya se imprimir mensajes en la consola")

#Escribir un programa que imprima por pantalla la suma de 1234 y 532.
a=1234 
b=532
c=a+b
print(f"La suma de {a} y {b} es {c}")

#Escribir un programa que imprima por pantalla los números del 1 al 10 000.
inicio=1
fin=10000
print("Los números del 1 al 10 000 son: ")
for i in range(inicio, fin+1):
    print(i)

#Escribir un programa que imprima por pantalla los cuadrados de los 30 primeros números naturales.
x=5
print(f"Los cuadrados de los {x} primeros números naturales son: ")
for i in range(1, x+1):
    print(f"El cuadrado de {i} es {i ** 2}")
