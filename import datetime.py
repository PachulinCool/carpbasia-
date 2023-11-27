import datetime
import csv

vehiculos = [["tipo", "placa", "dia", "hora"]]
vehregi = []

while True:
    accion = input("""¿Qué desea hacer?
                    1. Ingresar vehículo
                    2. Registrar salida
                    3. Salir\n""")
    
    if accion == "1":
        pal = input("Ingrese una placa: ")
        vehregi.append(pal)
        nv = []
        if pal.startswith("D"):
            nv.append("auto")
        elif pal.startswith("Q"):
            nv.append("moto")
        else:
            print("Tipo de vehículo no válido.")
            continue
        
        nv.append(pal)
        fecha_hora_actual = datetime.datetime.now()
        dia_actual = fecha_hora_actual.strftime("%Y-%m-%d")
        hora_actual = fecha_hora_actual.strftime("%H:%M:%S")
        nv.append(dia_actual)
        nv.append(hora_actual)
        tiempo_actual1 = fecha_hora_actual.timestamp()
        vehiculos.append(nv)
    
    elif accion == "2":
        pals = input("Ingrese una placa: ")
        if pals in vehregi:
            fecha_hora_actual = datetime.datetime.now()
            dia_actual = fecha_hora_actual.strftime("%Y-%m-%d")
            hora_actual = fecha_hora_actual.strftime("%H:%M:%S")
            tiempo_actual = fecha_hora_actual.timestamp()
            
            # You can calculate the time spent here using tiempo_actual and tiempo_actual1
            # Calculate the fee based on time spent if needed
            # Append the fee to the "cobro" list
            
            for fila, sublista in enumerate(vehiculos):
                if pals in sublista:
                    vehiculos.pop(fila)
                    break
        else:
            print("El vehículo no está registrado.")
    
    elif accion == "3":
        break

ruta_archivo = "vheiculos.csv"  # Use a relative path or specify the complete path
with open(ruta_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for fila in vehiculos:
        escritor_csv.writerow(fila)

print("Datos guardados en el archivo vheiculos.csv")
