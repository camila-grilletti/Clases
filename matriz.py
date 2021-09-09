class Matriz:
    def __init__(self):
        self.elementos=[0,1,2,3]
        self.matriz1 = []
        self.matriz2 = []
        self.matriz3 = []
    def ingresar(self):
        for i in self.elementos:
            n=int(input("Ingrese elementos para la primera matriz: "))
            self.matriz1.append(n)
        for j in self.elementos:
            m=int(input("Ingrese elementos para la segunda matriz: "))
            self.matriz2.append(n)
        print("Matriz 1: ", self.matriz1)
        print("Matriz 2: ", self.matriz2)
    def sumaMatrices(self):
        for i in range(len(self.matriz1)):
            self.matriz3.append(self.matriz1[i]+self.matriz2[i])
        return self.matriz3   

matriz = Matriz()
matriz.ingresar()
print("Suma de matrices: ", matriz.sumaMatrices())