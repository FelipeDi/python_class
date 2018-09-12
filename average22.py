cant=int(input("ingresar cantidad de personas"))
c=1
gmujer=0
ghombre=0
edusuario=0
edmujer=0
edhombre=0
while c<= cant:
    edad=float(input("ingrese su edad::::::"))
    genero=input("ingrese su genero <m/f>::::::")
    edusuario=edusuario+edad
    c=c+1
    promedio =edusuario / cant
    if genero == "m" :
        ghombre = ghombre + 1
        edhombre = edhombre + edad
    elif genero == "f" :
         gmujer = gmujer + 1
         edmujer = edmujer + edad
promehom = edhombre / ghombre
promujer = edmujer / gmujer
print("promedio de edades es:",promedio)
print("cantidad total de mugeres:",gmujer)
print("cantidad total de hombres:",ghombre)
print("promedio  edades de hombres :",promehom)
print("promedio  edades de mujeres :",promujer)
print("total de personas ingresadas en el sistema",cant)
        
    
