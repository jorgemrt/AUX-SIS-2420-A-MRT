
#1. Análisis de lista de números

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

# 2. Multiplicación de matrices

def multmat(a, b):
    if len(a[0]) != len(b):
        return None

    res = []
    for i in range(len(a)):
        fila = []
        for j in range(len(b[0])):
            s = 0
            for k in range(len(b)):
                s += a[i][k] * b[k][j]
            fila.append(s)
        res.append(fila)
    return res

a = [[6, 2], [7, 4]]
b = [[4, 9], [7, 2]]

r = multmat(a, b)

if r is None:
    print("No se puede multiplicar: dimensiones incompatibles.")
else:
    print("Resultado de la multiplicación:")
    for f in r:
        print(f)
#3. Transpuesta de una matriz
mrt = [[1, 2, 3], [4, 5, 6]]
rt = []
for i in range(len(mrt[0])):
    f = []
    for j in range(len(mrt)):
        f.append(mrt[j][i])
    rt.append(f)
print(rt)
 