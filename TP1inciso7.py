#7. Escribe un programa que tome una lista de números enteros como entrada del usuario. Luego,
# convierte cada número en la lista a string y únelos en una sola cadena, separados por guiones
# (‘-’). Sin embargo, excluye cualquier número que sea múltiplo de 3 de la cadena final.

# Programa que procesa una lista de números enteros

# Solicitar al usuario que ingrese una lista de números
entrada = input("Ingrese una lista de números enteros, separados por espacios: ")
numeros = list(map(int, entrada.split()))  # Convertir la entrada en una lista de enteros

# Convertir los números a string y unirlos en una sola cadena
resultado = '-'.join(str(n) for n in numeros if n % 3 != 0)

# Imprimir el resultado
print("Cadena resultante:", resultado)
