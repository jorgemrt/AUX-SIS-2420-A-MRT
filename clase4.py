
#1. Análisis de lista de números
##Escribe un programa que pida al usuario una lista de números separados por comas y luego
##calcule e imprima:
#- La suma de todos los números.
#- El número más grande y el más pequeño.
#- Cuántos números son pares y cuántos son impares.
entrada = input("ingrese numeros separados por una ( , ) que ser una lista")
lista_texto = entrada.split(",")
numeros = []
for texto in lista_texto:
    numeros.append(int(texto.strip()))
suma = 0
mayor = numeros[0]
menor = numeros[0]
pares = 0
impares = 0
for num in numeros:
    suma =suma +num
    if num > mayor:
        mayor = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        pares = pares +1
    else:
        impares =impares + 1

print("Suma ", suma)
print("Número más grande:", mayor)
print("Número más pequeño:", menor)
print("Números pares:", pares)
print("Números impares:", impares)