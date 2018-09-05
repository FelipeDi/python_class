
rango = 1
num =1
tabla_i = int(input("ingrese  la tabla  a resolver: "))
rango = int(input("ingrese el fin del rango: "))
while tabla_i <= rango :
	multip = 1
	while multip <= 10 :
		print (tabla_i ,"*", multip, "=", tabla_i * multip)
		multip = multip + 1
	tabla_i = tabla_i + 1