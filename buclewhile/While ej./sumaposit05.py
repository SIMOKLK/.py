#coding: utf-8
numero = int(input("Escriba un número: "))
suma = 0

while numero > 0:
    suma += numero
    numero = int(input("Escriba otro número: "))

print()
print("La suma de los números positivos introducidos es", str(suma) + ".")
print("Programa terminado")

