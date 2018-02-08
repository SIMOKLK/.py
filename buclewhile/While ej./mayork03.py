# coding: utf-8

primero = int(input("Escriba un número: "))
segundo = int(input("Escriba un número mayor que " + str(primero) + ": "))

while segundo > primero:
    primero = segundo
    segundo = int(input("Escriba un número mayor que " + str(primero) + ": "))

print("MAL")
print(segundo, "no es mayor que", str(primero) + ".")
print("Programa terminado")

