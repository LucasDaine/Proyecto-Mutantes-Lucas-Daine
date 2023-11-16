## matriz 6x6 
# letras A - T - C - G 

print("M A G N E T O   C O R P S\n")

while True:
    print("Ingrese el ADN (A,T,C,G) en mayúsculas")
    print("Recuerda que son 36 caracteres")
    matriz = list(input())
    contador = 0
    if (len(matriz) == 36):
        for letra in matriz:
            if (letra == "A" , "G" , "T" ,"C"):
                contador = contador + 1
    if (contador != 36):  
        print("parece que has ingresado mal los datos, intenta de nuevo\n")
    else: break

print("ANALIZANDO...\n")

print("su ADN es:\n")

##Charles Xavier me controló la mente y me hizo creer que podía resolver este
# trabajo sin la necesidad de crear una verdadera matriz... me equivoqué#

mutante = 0

def listas(matriz):
    for i in range (0,6):
        i = list()
        for j in range (0,6):
            i.append(matriz[j])
        print(i)

listas(matriz)

##le confirmo el resultado al usuario
if (mutante==1):
    print("Es Mutante")
else: print("No es Mutante")

# ATCGATCGATCGATCGATCGATCGATCGATCGAAAA#