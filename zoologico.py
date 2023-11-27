class zoolog():

    def __init__(self):
        self.li=[["especie", "edad", "tamaño", "peso", "altura", "fecha de ingreso", "género", "tipo de alimento", "horarios de comida", "vacunas", "enfermedades"]]
        self.tamaño=len(self.li)
        if self.tamaño<11:
            self.parametros()
        if self.tamaño>11:
            self.aa=input("ingrsara mas")
            if self.aa=="si":
                self.parametros()
        if self.tamaño==51:
            print("no hay mas cupos")
    def paramatros(self):
        self.l1=[]
        self.a=input("digite especie ")
        self.b=input("digite edad")
        self.c=input("digite tamaño")
        self.d=input("digite peso")
        self.e=input("digite altura")
        self.f=input("digite fecha de entrada")
        self.g=input("digite genero")
        self.h=input("digite tipo de alimentacion")
        self.i=input("digite horario de comida")
        self.j=input("digite vacunas")
        self.k=input("digite enfermedades")
        self.l1.append(self.a)
        self.l1.append(self.b)
        self.l1.append(self.c)
        self.l1.append(self.d)
        self.l1.append(self.e)
        self.l1.append(self.f)
        self.l1.append(self.g)
        self.l1.append(self.h)
        self.l1.append(self.i)
        self.l1.append(self.j)
        self.l1.append(self.k)
        print(self.l1)
        self.li.append(self.l1)


class guar(zoolog):
    def __init__(self):
        super(). __init__() 
        print("adios")
b=guar()
