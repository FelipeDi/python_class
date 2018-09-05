
rango = 1
num = 1

tabla = int( input ( "ingrese  la tabla  a resolver: " ))
tabla = int( input ( "ingrese el fin del rango: " ))
while tabla <= tabla_max :
	multip = 1
	while multip <= 10 :
		print (tabla ,"*", multip, "=", tabla * multip)
		multip = multip + 1
	tabla = tabla + 1