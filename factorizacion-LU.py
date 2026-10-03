# ============================================
# FACTORIZACIÓN LU DE UNA MATRIZ 3x3
# MÉTODO DE DOOLITTLE
# Acepta enteros, decimales y fracciones
# ============================================
from fractions import Fraction

print("======================================")
print("   FACTORIZACIÓN LU DE UNA MATRIZ 3x3")
print("           MÉTODO DE DOOLITTLE")
print("======================================")
print()
print("Ejemplos de datos válidos:")
print("Entero:     5")
print("Decimal:    2.5")
print("Fracción:   3/4")
print("Fracción:  -5/2")
print()

# ============================================
# FUNCIÓN PARA INGRESAR LOS NÚMEROS
# ============================================

def ingresar_numero(mensaje):

    while True:

        dato = input(mensaje).strip()

        try:

            # Si contiene una fracción
            if "/" in dato:

                partes = dato.split("/")

                # Verificar que tenga numerador y denominador
                if len(partes) != 2:
                    raise ValueError

                numerador = int(partes[0].strip())
                denominador = int(partes[1].strip())

                # Evitar división entre cero
                if denominador == 0:
                    print("Error: el denominador no puede ser cero.")
                    continue

                return Fraction(numerador, denominador)

            # Si es decimal o entero
            else:

                return Fraction(dato)

        except ValueError:

            print()
            print("Dato incorrecto.")
            print("Ingrese un número entero, decimal o fracción.")
            print("Ejemplos: 5, 2.5, 3/4, -7/3")
            print()


# ============================================
# INGRESAR MATRIZ A
# ============================================

print("INGRESE LOS ELEMENTOS DE LA MATRIZ A")
print("--------------------------------------")

a11 = ingresar_numero("Ingrese a11: ")
a12 = ingresar_numero("Ingrese a12: ")
a13 = ingresar_numero("Ingrese a13: ")

a21 = ingresar_numero("Ingrese a21: ")
a22 = ingresar_numero("Ingrese a22: ")
a23 = ingresar_numero("Ingrese a23: ")

a31 = ingresar_numero("Ingrese a31: ")
a32 = ingresar_numero("Ingrese a32: ")
a33 = ingresar_numero("Ingrese a33: ")


# ============================================
# MATRIZ A
# ============================================

A = [
    [a11, a12, a13],
    [a21, a22, a23],
    [a31, a32, a33]
]


# ============================================
# MATRIZ L
# ============================================

L = [
    [Fraction(1), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(1), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(1)]
]


# ============================================
# MATRIZ U
# ============================================

U = [
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0)],
    [Fraction(0), Fraction(0), Fraction(0)]
]


# ============================================
# FACTORIZACIÓN LU
# MÉTODO DE DOOLITTLE
# ============================================

# Primera fila de U

U[0][0] = A[0][0]
U[0][1] = A[0][1]
U[0][2] = A[0][2]


# Verificar primer pivote

if U[0][0] == 0:

    print()
    print("No se puede realizar la factorización LU.")
    print("El primer pivote es cero.")

else:

    # Primera columna de L

    L[1][0] = A[1][0] / U[0][0]
    L[2][0] = A[2][0] / U[0][0]


    # Segunda fila de U

    U[1][1] = A[1][1] - L[1][0] * U[0][1]

    U[1][2] = A[1][2] - L[1][0] * U[0][2]


    # Verificar segundo pivote

    if U[1][1] == 0:

        print()
        print("No se puede realizar la factorización LU.")
        print("El segundo pivote es cero.")

    else:

        # Segunda columna de L

        L[2][1] = (
            A[2][1] - L[2][0] * U[0][1]
        ) / U[1][1]


        # Tercera fila de U

        U[2][2] = (
            A[2][2]
            - L[2][0] * U[0][2]
            - L[2][1] * U[1][2]
        )


        # ====================================
        # FUNCIÓN PARA MOSTRAR MATRICES
        # ====================================

        def mostrar_matriz(nombre, matriz):

            print()
            print(nombre)

            for fila in matriz:

                print("[", end=" ")

                for elemento in fila:

                    print(f"{elemento}", end=" ")

                print("]")


        # ====================================
        # MOSTRAR RESULTADOS
        # ====================================

        mostrar_matriz("MATRIZ A:", A)

        mostrar_matriz("MATRIZ L:", L)

        mostrar_matriz("MATRIZ U:", U)


        print()
        print("======================================")
        print("FACTORIZACIÓN:")
        print("A = L × U")
        print("======================================")