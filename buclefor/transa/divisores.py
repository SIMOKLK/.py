#coding: utf-8

print("DIVISORES")
numero = int(input("Escriba un número entero mayor que cero: "))

if numero <= 0:
    print("¡Le he pedido un número entero mayor que cero!")
else:
    print("Los divisores de {numero} son ", end=" ")
    for i in range(1, round(numero/2)+1):
        if numero % i == 0:
            print(i, end=" ")
    print(numero)

