#coding: utf-8

primero = int(input("Escriba un número: "))
segundo = int(input("Escriba un número mayor que " + str(primero) + ": "))

while segundo <= primero:
    print(segundo, "no es mayor que", str(primero) + ". Inténtelo de nuevo: )
    segundo = int(input())

print()
print("Los números que ha escrito son", primero, "y", str(segundo) + ".")
print("Programa terminado")
