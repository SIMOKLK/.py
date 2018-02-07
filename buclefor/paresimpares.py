#coding: utf-8


print("PARES E IMPARES")
numero_1 = int(input("Escriba un número entero: "))
numero_2 = int(input("Escriba un número entero mayor o igual que {numero_1}: "))

if numero_2 < numero_1:
    print("¡Le he pedido un número entero mayor o igual que {numero_1}!")
else:
    for i in range(numero_1, numero_2 + 1):
        if i % 2 == 0:
            print("El número es par")
        else:
            print("El número  es impar")


