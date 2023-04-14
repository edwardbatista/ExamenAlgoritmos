import math

#Algoritmo de ordenamiento Bubble Sort
def ordenamiento(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Función iterativa para sumar pares de números
def sumar_pares(arr):
    suma = 0
    for i in range(0, len(arr), 2):
        suma += arr[i] + arr[i+1]
    return suma

#Función recurisva para sumar pares de números
def sumar_pares_recursiva(arr, index=0):
    if index >= len(arr) - 1:
        return 0
    elif index + 1 < len(arr):
        return arr[index] + arr[index+1] + sumar_pares_recursiva(arr, index+2)
    else:
        return arr[index]

#Función para resolver la ecuación exponencial
def resolver_ecuacion_exponencial(arr):
    suma1 = sumar_pares(arr[0:2])
    suma2 = sumar_pares_recursiva(arr[2:4])
    suma3 = sumar_pares(arr[4:6])
    if suma1 == (2 * suma2) - suma3:
      base = arr[0]
      resultado = arr[1]
      if (base == 0) or (base == 1):
        return f"Suma 1: {arr[0]} + {arr[1]} = {suma1}\nSuma 2: {arr[2]} + {arr[3]} = {suma2}\nSuma 3: {arr[4]} + {arr[5]} = {suma3}\nCondición: {suma1} = (2 * {suma2}) - {suma3}\n{suma1} = {(2 * suma2) - suma3}\nSe satisface la condición pero el primer elemento (la base) es 0 o 1, lo que significa que este problema está indefinido para {base}^x = {resultado}."

      else:
        exponente = math.log(resultado, base)
        return f"Suma 1: {arr[0]} + {arr[1]} = {suma1}\nSuma 2: {arr[2]} + {arr[3]} = {suma2}\nSuma 3: {arr[4]} + {arr[5]} = {suma3}\nCondición: {suma1} = (2 * {suma2}) - {suma3}\n{suma1} = {(2 * suma2) - suma3}\nSe satisface la condición, aquí la ecuación exponencial resultante: {base}^{exponente} = {resultado}"

    else:
      return f"Suma 1: {arr[0]} + {arr[1]} = {suma1}\nSuma 2: {arr[2]} + {arr[3]} = {suma2}\nSuma 3: {arr[4]} + {arr[5]} = {suma3}\nCondición: {suma1} = (2 * {suma2}) - {suma3}\n{suma1} = {(2 * suma2) - suma3}\nNo se cumple la condición."


#Busqueda de Boyer-Moore
def boyer_moore_no(text):
    pattern = "No se cumple"
    n = len(text)
    m = len(pattern)
    if m == 0:
        return True
    if n < m:
        return False

    bad_char = {}
    for i in range(m-1):
        bad_char[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            return True
        if text[i] in bad_char:
            i += bad_char[text[i]]
        else:
            i += m

    return False

#Busqueda de Boyer-Moore
def boyer_moore_si(text):
    pattern = "Se satisface"
    n = len(text)
    m = len(pattern)
    if m == 0:
        return True
    if n < m:
        return False

    bad_char = {}
    for i in range(m-1):
        bad_char[pattern[i]] = m - i - 1

    i = m - 1
    while i < n:
        j = m - 1
        while j >= 0 and text[i] == pattern[j]:
            i -= 1
            j -= 1
        if j == -1:
            return True
        if text[i] in bad_char:
            i += bad_char[text[i]]
        else:
            i += m

    return False



# Solicitar al usuario la cantidad de arreglos que desea ingresar
cantidad_arreglos = int(input("Ingrese la cantidad de arreglos que desea ingresar: "))

# Inicializar una lista vacía para almacenar los arreglos del usuario
arreglos_usuario = []

# Solicitar al usuario que ingrese los arreglos de 6 números
for i in range(cantidad_arreglos):
    # Leer los números del usuario como una cadena de texto
    numeros = input(f"Ingrese 6 números separados por espacios para el arreglo {i+1}: ")
    # Convertir la cadena de texto en una lista de enteros
    arreglo = list(map(int, numeros.split()))
    # Agregar el arreglo a la lista de arreglos del usuario
    arreglos_usuario.append(arreglo)

#Contadores de condición
nocumple = 0
sicumple = 0

# Procesamiento de los datos de prueba
for i, datos in enumerate(arreglos_usuario):
  print(f"Datos de prueba {i+1} sin ordenar: {datos}")
  print(f"Datos de prueba {i+1} ordenados: {datos}")
  resultado = resolver_ecuacion_exponencial(datos)
  print(resultado)
  print("---")
  if boyer_moore_no(resolver_ecuacion_exponencial(datos)):
    nocumple += 1
  if boyer_moore_si(resolver_ecuacion_exponencial(datos)):
    sicumple += 1

print(f"\n\nLa cantidad de arreglos que cumplieron con la condición fue: {sicumple}")
print(f"La cantidad de arreglos que no cumplieron con la condición fue: {nocumple}")
