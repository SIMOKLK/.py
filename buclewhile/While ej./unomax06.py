#coding: utf-8
limite = float(input("Escriba el valor límite: "))
while limite <= 0:
    limite = float(input("El límite debe ser mayor que 0. Inténtelo de nuevo: "))

numero = float(input("Escriba un número: "))
suma = 0
suma += numero

while suma < limite:
    numero = float(input("Escriba otro número: "))
    suma += numero

print()
print("Ha superado el límite. La suma de los números positivos introducidos es", str(suma) + ".")
print("Programa terminado")
