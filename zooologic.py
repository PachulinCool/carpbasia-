class Zoolog():
    def __init__(self):
        self.li = [["especie", "edad", "tamaño", "peso", "altura", "fecha de ingreso", "género", "tipo de alimento", "horarios de comida", "vacunas", "enfermedades"]]
        self.tamaño = len(self.li)
        
        while self.tamaño < 51:
            if self.tamaño<11:
                self.parametros()
            if self.tamaño>11:
                self.aa=input("presione 1 para seguir")
                if self.aa==1:
                    self.parametros()
                else:
                    break
            if self.tamaño==50:
                print("No hay más cupos")
                break

    def parametros(self):
        self.l1 = []
        self.a = input("Digite especie: ")
        self.b = input("Digite edad: ")
        self.c = input("Digite tamaño: ")
        self.d = input("Digite peso: ")
        self.e = input("Digite altura: ")
        self.f = input("Digite fecha de entrada: ")
        self.g = input("Digite género: ")
        self.h = input("Digite tipo de alimentación: ")
        self.i = input("Digite horario de comida: ")
        self.j = input("Digite vacunas (separadas por comas): ")
        self.k = input("Digite enfermedades (separadas por comas): ")
        
        self.l1.extend([self.a, self.b, self.c, self.d, self.e, self.f, self.g, self.h, self.i, self.j, self.k])
        print(self.l1)
        self.li.append(self.l1)

class Guar(Zoolog):
    def __init__(self):
        super().__init__()
        print("Adiós")

b = Guar()

