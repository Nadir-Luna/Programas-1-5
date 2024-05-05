print("Contador de palabras")

frase = str(input("ingresa una frase: "))

cant_palabras = frase.split()

resultado = len(cant_palabras)

print(f"La cantidad de palabras de la frase es: {resultado}")