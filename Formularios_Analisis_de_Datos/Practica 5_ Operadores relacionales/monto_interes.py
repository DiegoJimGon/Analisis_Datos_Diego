monto=float(input("ingrese monto en pesos"))
interes=float(input("ingrese interes (1-30"))
#intereses=0
interes=interes*0.01
#print(interes)

if(interes<=0.3):
    print(f"monto:{monto}")
#   print(f"importe total:")
    intereses=monto*interes
    print(f"interes:{intereses}")
    print(f"el monto + interes= {monto+intereses}")
else:
    print("el interes es incorrecto")
    