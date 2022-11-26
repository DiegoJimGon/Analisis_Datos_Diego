n=int(input("ingresa un numero "))

if(1<=n and n<=7):
    print(f"el numero,{n}  está EN EL RANGO de 1 a 7")
    
else:
    print(f"el numero :{n} está FUERA DEL RANGO (1-7)")
    if(n<1):
        print(f"{n} es menor al rango 1 al 7")
    else:
        print(f"{n} es mayor al rango 1 al 7")