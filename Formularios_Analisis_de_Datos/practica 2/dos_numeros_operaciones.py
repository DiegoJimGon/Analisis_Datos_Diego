numero_1=int(input("introduce un número"))
numero_2=int(input("introduce otro número"))

print(f"suma")
print(f"{numero_1}+{numero_2}={numero_1+numero_2}")
print(f"resta")
print(f"{numero_1}-{numero_2}={numero_1-numero_2}")
print(f"multiplicación")
print(f"{numero_1}*{numero_2}={numero_1*numero_2}")
if(numero_2==0):
    print(f"numero no se puede dividir entre 0")
else:
    print(f"{numero_1}/{numero_2}={numero_1/numero_2}")