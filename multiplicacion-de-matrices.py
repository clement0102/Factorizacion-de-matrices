# ==========================================
# MULTIPLICACIÓN DE DOS MATRICES 3x3
# Admite enteros, decimales y fracciones
# ==========================================

print("==========================================")
print("     MULTIPLICACIÓN DE MATRICES 3x3")
print("==========================================")
print("Puede ingresar:")
print("Enteros: 5")
print("Decimales: 2.5")
print("Fracciones: 1/2")
print("==========================================")


# ------------------------------------------
# FUNCIÓN PARA LEER LOS NÚMEROS
# ------------------------------------------

def leer_numero():
    entrada = input("Ingrese el número: ")

    if "/" in entrada:
        partes = entrada.split("/")

        numerador = float(partes[0])
        denominador = float(partes[1])

        return numerador / denominador

    else:
        return float(entrada)


# ------------------------------------------
# INGRESO DE LA MATRIZ A
# ------------------------------------------

print("\nINGRESO DE LA MATRIZ A")
print("----------------------")

A = []

for i in range(3):

    fila = []

    for j in range(3):

        print(f"A[{i+1}][{j+1}]")
        numero = leer_numero()

        fila.append(numero)

    A.append(fila)


# ------------------------------------------
# INGRESO DE LA MATRIZ B
# ------------------------------------------

print("\nINGRESO DE LA MATRIZ B")
print("----------------------")

B = []

for i in range(3):

    fila = []

    for j in range(3):

        print(f"B[{i+1}][{j+1}]")
        numero = leer_numero()

        fila.append(numero)

    B.append(fila)


# ------------------------------------------
# MOSTRAR MATRIZ A
# ------------------------------------------

print("\nMATRIZ A")
print("--------")

for fila in A:
    print(fila)


# ------------------------------------------
# MOSTRAR MATRIZ B
# ------------------------------------------

print("\nMATRIZ B")
print("--------")

for fila in B:
    print(fila)


# ------------------------------------------
# CREAR MATRIZ RESULTADO
# ------------------------------------------

C = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]


# ------------------------------------------
# MULTIPLICACIÓN DE MATRICES
# ------------------------------------------

for i in range(3):

    for j in range(3):

        for k in range(3):

            C[i][j] = C[i][j] + A[i][k] * B[k][j]


# ------------------------------------------
# MOSTRAR RESULTADO
# ------------------------------------------

print("\n==========================================")
print("           MATRIZ RESULTADO")
print("==========================================")

for fila in C:
    print([round(numero, 4) for numero in fila])