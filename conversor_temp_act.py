print("Este es un conversor de grados Celcius a Farenheit o viceversa")

tipo_conversion = int(input("Elige si quieres convertir grados celsius a farenheit (1) o viceversa (2):"))

if tipo_conversion == 1:
    temp_celcius = float(input("Ingrese la temperatura en grados celcius: "))
    conversión = (temp_celcius * 9/5) + 32
    print(f"la temperatura en grados Farenheit es {conversión}")
else :
    temp_farenheit = float(input("Ingrese la temperatura en grados farenheit: "))
    conversión_2 = (temp_farenheit - 32) * 5/9
    print(f"La temperatura en grados celcius es {conversión_2}")





