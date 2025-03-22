class Animal :
    def __init__(self,tamaniox,colorx,tipoanimalx): 
        self.tamanio = tamaniox
        self.tipoanimal = tipoanimalx
        self.color =colorx
    def planilla(self):
        print("hola soy un "+self.tipoanimal+".tengo el tamanio de : "+self.tamanio+".y tengo un color "+self.color)
    datos=Animal("10","BLANCO","GATO")
    print(datos.planilla())









