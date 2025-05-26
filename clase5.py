class Animal:
    def __init__(self, nom, edad):
        self.nom = nom
        self.edad = edad
    def EmiSonido(self):
        print("Este animal hace un sonido")
class Perro(Animal):
    def EmiSonido(self):
        print("Guau Guau")
class Gato(Animal):
    def EmiSonido(self):
        print("Miau")
class Pajaro(Animal):
    def EmiSonido(self):
        print("Pío pío")
def EmitirSonido(animales: list):
    for animal in animales:
        animal.EmiSonido()
if __name__ == "__main__":
    mi_perro = Perro("Rex", 3)
    mi_gato = Gato("Misi", 2)
    mi_pajaro = Pajaro("Piolín", 1)
    animales = [mi_perro, mi_gato, mi_pajaro]
    EmitirSonido(animales)