import matplotlib.pyplot as plt
import numpy as np

# Datos de la probabilidad conjunta f(X,Y)
X = [1, 2, 3]
Y = [1, 2, 3]
f_XY = np.array([[0.12, 0.16, 0.12], [0.105, 0.14, 0.105], [0.075, 0.1, 0.075]])

# Cálculo de las probabilidades de Z = X + Y
Z = [2, 3, 4, 5, 6]
f_Z = [0.12, 0.265, 0.335, 0.205, 0.075]

# Cálculo de las probabilidades de W = X - Y
W = [-2, -1, 0, 1, 2]
f_W = [0.12, 0.265, 0.335, 0.205, 0.075]

# Gráficas
plt.figure(figsize=(10, 8))

# Gráfica de f_XY
plt.subplot(2, 1, 1)
X_grid, Y_grid = np.meshgrid(X, Y)
plt.pcolormesh(X_grid, Y_grid, f_XY, shading='auto', cmap='viridis')
plt.title('Función de Masa de Probabilidad Conjunta f_XY')
plt.xlabel('X')
plt.ylabel('Y')
plt.colorbar(label='Probabilidad')

# Gráfica de f_Z
plt.subplot(2, 1, 2)
plt.stem(Z, f_Z, basefmt=" ", use_line_collection=True)
plt.title('Función de Masa de Probabilidad f_Z')
plt.xlabel('Z')
plt.ylabel('Probabilidad')
plt.grid(True)

plt.tight_layout()
plt.show()
