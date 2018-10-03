def menu():
	print("menu aritmetico")
	print ("1. sumar:")
	print ("2. restar:")
	print ("3. multiplicar:")
	print ("4. dividir:")
	print ("5. raiz cuadrada")
def datos():
	global n1,n2
	n1 = int(input("ingrese el 1er.numero:"))
	n2 = int(input("ingrese el 2do.numero:"))

def operaciones():
	if opc== 1:
		print("el resultado de la suma:",n1+n2)
	elif opc== 2:
		print("el resultado de la resta:",n1-n2)
	elif opc== 3:
		print("la multiplicacion es:",n1*n2)
	elif opc== 4:
		print("la division es:",n1/n2)
	elif opc== 5:
		rc=n1**(1/2)
		rc=n2**(1/2)
		print("la raiz cuadrada es:",n1**(1/2))
		print("la raiz caudrada es: ",n2**(1/2))

datos()
menu()
opc = int(input("digite su opcion:"))
operaciones()