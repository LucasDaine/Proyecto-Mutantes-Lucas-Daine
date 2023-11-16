print("M A G N E T O   C O R P S\n")

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

print("ANALIZANDO...\n")

print("su ADN es:\n")

contFilas = 0
contColum = 0
for elemento in matriz:
    contFilas = contFilas + 1
    print("[",elemento,end=" ]")
    if (contFilas > 5):
        print("\n")
        contFilas = 0

mutante = 0

conteoH = 1
for i in range (0,5):
    for j in range (0,5):
        if (matriz[j] == matriz[j+1]):
            conteoH = conteoH+1
            if (conteoH == 4):
                print("Es Mutante")
                break
            else: mutante = 0

conteoV = 1
for i in range (0,5):
    for j in range (0,5):
        if (matriz[i] == matriz[i+6]):
            conteoV = conteoV+1
            if (conteoV == 4):
                print("Es Mutante")
                break
            else: mutante = 0



## matriz 6x6 
# letras A - T - C - G 
# ATCGTCATCGCTACGTCGACGTCGATGCTCATGCTC#