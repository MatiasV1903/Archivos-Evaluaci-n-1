vlan = int(input("Ingrese un numero de VLAN: "))
if (vlan >= 0 and vlan <= 1005):
    print("La VLAN es de rango NORMAL")
elif (vlan >= 1006 and vlan <= 4095 ):
    print(" La VLAN es de rango EXTENDIDA")
else:
    print("Digito ingresado no es valido")