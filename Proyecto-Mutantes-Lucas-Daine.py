print("M A G N E T O   C O R P S")

while True:
    print("Ingrese su ADN (A,T,C,G) en mayúsculas")
    matriz = list(input())
    contador = 0
    if (len(matriz) == 36):
        for letra in matriz:
            if (letra == "A" , "G" , "T" ,"C"):
                contador = contador + 1
    if (contador != 36):  
        print("parece que has ingresado mal los datos, intenta de nuevo")
    else: break

print("ANALIZANDO...")

print("su ADN es:")

contFilas = 0
contColum = 0
for elemento in matriz:
    contFilas = contFilas + 1
    print("[",elemento,end=" ]")
    if (contFilas > 5):
        print("\n")
        contFilas = 0





## matriz 6x6 
# letras A - T - C - G 
# ATCGATCGATCGATCGATCGATCGATCGATCGATCG#