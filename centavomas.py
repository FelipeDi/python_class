print("bienvenido a un centavomas:")
clave1='2001'
intentos=3
i=1
saldo=2000000
while i<=intentos :
    clave2=input("digite clave:")
    if clave1==clave2:
        print("menu transaccional:")
        print("1. cambiar clave:")
        print("2. mostrar saldo:")
        print("3. realizar retiro:")
        print("4. salir:")
    else:
        if i<intentos:
            print("clave incorrecta.Digite nuevamente")
        else:
            print ("usted no tiene mas intentos. Su tarjeta fue bloqueada")
        i=i+1
    opc=int(input("digite opcion"))
    if opc==1 :
        print("cambiar clave:")
    elif opc==2 :
        print("saldo de la cuenta",saldo)
    elif opc==3 :
        print("valor a retirar")
        print("1. $10.000")
        print("2. $20.000")
        print("3. $50.000")
        print("4. $100.000")
        print("5. $200.000")
        print("6. $400.000")
        print("7. $600.000")
        print("8. $1.000.000")
        sub=int(input("digite opcion:"))
        if sub==1:
            saldon=saldo-10000
            print("valor extraido $10.000")
            print("saldo total es",saldon)
            if saldon<0:
                print("no cuenta con el suficiente dinero")
        elif sub==2:
            saldon1=saldo-20000
            print("valor extraido $20.000 ")
            print("saldo total es",saldon1)
            if saldon1<0:
                print("no cuenta con el suficiente dinero")
        elif sub==3:
            saldon2=saldo-50000
            print("valor extraido $50.000")
            print("saldo total es",saldon2)
            if saldon2<0:
                print("no cuenta con el suficiente dinero")
        elif sub == 4:
            saldon3=saldo-100000
            print ("valor extraido $100.000")
            print ("saldo total es: ",saldon3)
        elif sub==5:
            saldon4=saldo-200000
            print("valor extraido $200.000 ")
            print("saldo total es",saldon4)
            if saldon4<0:
                print("no cuenta con el suficiente dinero")
        elif sub==6:
            saldon5=saldo-400000
            print("valor extraido $400.000 ")
            print("saldo total es",saldon5)
            if saldon5<0:
                print("no cuenta con el suficiente dinero")
        elif sub==7:
            saldon6=saldo-600000
            print("valor extraido $600.000 ")
            print("saldo total es",saldon6)
            if saldon6<0:
                print("no cuenta con el suficiente dinero")
        elif sub==8:
            saldon7=saldo-1000000
            print("valor extraido $1.000.000 ")
            print("saldo total es",saldon7)
            if saldon7<0:
                print("no cuenta con el suficiente dinero")
        break
