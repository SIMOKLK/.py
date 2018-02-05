#coding: utf-8

minimo = int(input("Escriba un número: "))
maximo = int(input("Escriba un número mayor que " + str(minimo) + ": "))
while minimo >= maximo:
    maximo = int(input(str(maximo) + " no es mayor que " + str(minimo) + ".Inténtelo de nuevo: "))

numero = float(input("Escriba un número entre " + str(minimo) + " y " + str(maximo) + ": "))
contador = 0

while minimo <= numero <= maximo:
    contador += 1
    numero = float(input("Escriba un número entre " + str(minimo) + " y " + str(maximo) + ": "))

print()
if contador == 0:
    print("No ha escrito ningún número entre", minimo, "y", str(maximo) + ".")
elif contador == 1:
    print("Ha escrito 1 número entre", minimo, "y", str(maximo) + ".")
else:
    print("Ha escrito", contador, "números entre", minimo, "y", str(maximo) + ".")
print("Programa terminado")
