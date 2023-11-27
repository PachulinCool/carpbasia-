import sys

def serie ():
    if len(resis)<2:
        sys.exit()
    print("a")
    print(resis)
    print("su resistencia equivalente es:")
    print(suma)
    v=float(input("voltage"))
    i=(int(v)/h)
    print("su corriente es:")
    print(i)
    pcon=v*i
    print("su potencia es :")
    print(pcon)
a=serie    

def paralelo():
    print(1)
    if len(resis)<2:
        sys.exit()
    print("a")
    print(resis)
    print("su resistencia equivalente es:")
    print(suma)
    v=float(input("voltage"))
    i=(float(v)/h)
    print("su corriente es:")
    print(i)
    pcon=v*i
    print("su potencia es :")
    print(pcon)

b=paralelo    


while True:
    c=input("1.serie o 2.paralelo")
    if c=="1":
        resis=[]
        while True:
            vr=float(input("diguite el valor de la resistencia"))
            resis.append(vr)
            se=input("desea ingresar otra resistencia")
            if se == "no":
                suma = float(sum(resis))
                h=float(suma)
                break
        serie()
    if c=="2":
        resis=[]
        while True:
            vr=float(input("diguite el valor de la resistencia"))
            resis.append(1/vr)
            se=input("desea ingresar otra resistencia")
            if se == "no":
                suma=float(1/sum(resis))
                h=float(suma)
                break

        paralelo()

