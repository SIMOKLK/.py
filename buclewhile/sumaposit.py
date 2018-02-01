#coding: utf-8
num = int(input("Escribe un numero:"))
suma=0

while num > 0:
	suma+= num
	num2 = int(input("Otro numero:"))
	print "la suma de los numeros positivos es", str(suma) + "."
