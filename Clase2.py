# PEDIR NUMEROS  HASTA QUE SE  INGRESE UN NUMERO NEGATIVO
numeros = []
num = 0
while num >= 0:
    num = int(input("Ingresa un número: "))
    if num >= 0:
        numeros =  numeros +[num]  
print("numeros positivos :", numeros)

