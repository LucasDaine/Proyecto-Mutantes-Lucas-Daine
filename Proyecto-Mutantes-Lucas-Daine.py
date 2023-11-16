## matriz 6x6 
# letras A - T - C - G 
print("")
print("M A G N E T O   C O R P S\n")

##PEDIMOS AL USUARIO INGRESAR EL ADN
while True:
    print("Ingrese el ADN (A,T,C,G) en mayúsculas")
    print("Recuerda que son 36 caracteres\n")
    matriz = list(input())
    contador = 0
    if (len(matriz) == 36):
        for letra in matriz:
            if (letra == "A" , "G" , "T" ,"C"):
                contador = contador + 1
    if (contador != 36):  
        print("parece que has ingresado mal los datos, intenta de nuevo\n")
    else: break

##MOSTRAMOS POR PANTALLA UNA TABLITA

print("su ADN es:\n")

contador = 0
for elemento in matriz:
    contador = contador+1 
    print ("[",elemento,end=" ]")
    if (contador == 6):
        contador = 0
        print ("\n")

mutante = 0
coincidenciaMutante = 0

conteoH = 1
f=0
c=5
for i in range (0,6):
    for j in range (f,c):
        if (matriz[j] == matriz[j+1]):
            conteoH = conteoH+1
            if (conteoH == 4):
                coincidenciaMutante = coincidenciaMutante + 1
                mutante = 1
                break
    f=f+6
    c=c+6

conteoV = 1
f=0
c=6
for i in range (f,c):
    for j in range (0,6):
        if (matriz[j] == matriz[j+6]):
            conteoV = conteoV+1
            if (conteoV == 4):
                coincidenciaMutante = coincidenciaMutante + 1
                mutante = 1
                break
    f=f+6
    c=c+6


##le confirmo el resultado al usuario
if (mutante==1):
    print(coincidenciaMutante," Coincidencias Mutantes Encontradas, Es Mutante")
else: print("No es Mutante")

# ATCGATCGATCTATCGATCGATCTATCGATCGAAAA#