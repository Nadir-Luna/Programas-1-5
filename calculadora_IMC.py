print("Calculadora de Indice de Masa Corporal")
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

IMC = peso/altura**2

print(f"Tu IMC es igual a {IMC}, que tengas buen día :).")