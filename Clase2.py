# PEDIR NUMEROS  HASTA QUE SE  INGRESE UN NUMERO NEGATIVO
numeros = []
num = 0
while num >= 0:
    num = int(input("Ingresa un número: "))
    if num >= 0:
        numeros =  numeros +[num]  
print("numeros positivos :", numeros)

# PEDIR 5 NUMEROS  Y GUARDARLOS EN UNA LISTA E IMRIMIR LA SUMA Y EL PROMEDIO

sum = 0 
for i in range(5):
    numero = float(input("Ingresa un número: "))  
    sum = sum + numero 
promedio = sum / 5 
print("Suma:", sum)  
print("Promedio:", promedio)  