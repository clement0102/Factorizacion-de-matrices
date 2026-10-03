# FACTORIZACIÓN LU DE UNA MATRIZ 3x3
# Método de Doolittle

print("======================================")
print("   FACTORIZACIÓN LU DE UNA MATRIZ 3x3")
print("======================================")

# Ingreso de los elementos de la matriz A

a11 = float(input("Ingrese a11: "))
a12 = float(input("Ingrese a12: "))
a13 = float(input("Ingrese a13: "))

a21 = float(input("Ingrese a21: "))
a22 = float(input("Ingrese a22: "))
a23 = float(input("Ingrese a23: "))

a31 = float(input("Ingrese a31: "))
a32 = float(input("Ingrese a32: "))
a33 = float(input("Ingrese a33: "))

# Matriz A
A = [
    [a11, a12, a13],
    [a21, a22, a23],
    [a31, a32, a33]
]

# Matriz L
L = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

# Matriz U
U = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Primera fila de U
U[0][0] = A[0][0]
U[0][1] = A[0][1]
U[0][2] = A[0][2]

# Primera columna de L
if U[0][0] == 0:
    print("No se puede realizar la factorización LU sin pivoteo.")
else:
    L[1][0] = A[1][0] / U[0][0]
    L[2][0] = A[2][0] / U[0][0]

    # Segunda fila de U
    U[1][1] = A[1][1] - L[1][0] * U[0][1]
    U[1][2] = A[1][2] - L[1][0] * U[0][2]

    # Segunda columna de L
    if U[1][1] == 0:
        print("No se puede realizar la factorización LU sin pivoteo.")
    else:
        L[2][1] = (A[2][1] - L[2][0] * U[0][1]) / U[1][1]

        # Tercera fila de U
        U[2][2] = A[2][2] - L[2][0] * U[0][2] - L[2][1] * U[1][2]

        # Mostrar matriz A
        print("\nMatriz A:")
        for fila in A:
            print(fila)

        # Mostrar matriz L
        print("\nMatriz L:")
        for fila in L:
            print(fila)

        # Mostrar matriz U
        print("\nMatriz U:")
        for fila in U:
            print(fila)

        print("\nFactorización:")
        print("A = L × U")