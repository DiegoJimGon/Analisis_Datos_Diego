base=float(input("introduce valor de base(valor mayor a altura"))
altura=float(input("introduce valor de  altura"))
perimetro=base*2+altura*2
area=base*altura


if(altura<base or base< altura):
#   perimetro=base*2+altura*2
#   area=base*altura
    print(f"perimetro={perimetro} area={area}")
elif(base==altura):
    print("valor de la base no corresponde a un rectangulo")
