class Cinema:
    def __init__(self):
        self.peliculas = {
            "peli1": "11.30am",
            "peli2": "02.00pm",
            "peli3": "04.30pm",
            "peli4": "07.00pm"
        }
        self.alimentos = {
            "alimento1": "2000",
            "alimento2": "4000",
            "alimento3": "6000",
            "alimento4": "8000"
        }
        self.proximas_peliculas = ["proxima1", "proxima2", "proxima3", "proxima4"]
        self.empleados = {"lalo": "1234", "jhon": "5674"}
        self.cupones = 0

        self.contadores_tikets = [0, 0, 0, 0]
        self.contadores_alimentos = [0, 0, 0, 0]

        while self.cupones < 50:
            self.cl = input("""
                Si es empleado, digite 0.
                Si es cliente:
                ¿Qué tipo de cliente es usted?
                1. Cliente Frecuente
                2. Visitante

                Si es administrador, digite su contraseña: """)
            if self.cl == "0":
                self.empleado()
            elif self.cl == "1":
                self.menu_cliente_frecuente()
            elif self.cl == "2":
                self.menu_visitante()
            elif self.cl == "god":
                self.admin()

    def empleado(self):
        # Implementa la lógica para el empleado aquí
        pass

    def menu_cliente_frecuente(self):
        self.usua = input("Digite su usuario: ")
        self.contra = input("Digite su contraseña: ")
        if self.usua in self.empleados and self.empleados[self.usua] == self.contra:
            self.accfre = input("""
                ¿Qué desea hacer?
                1. Ver lista de películas
                2. Comprar tiquetes
                3. Comprar comidas
                4. Reservar películas
                """)

            if self.accfre == "1":
                print("Lista de películas:")
                for pelicula, hora in self.peliculas.items():
                    print(f"{pelicula}: {hora}")

            elif self.accfre == "2":
                print("Lista de películas:")
                for pelicula, _ in self.peliculas.items():
                    print(pelicula)
                pelicula_elegida = input("¿De qué película desea el tiquete? (peli1, peli2, peli3, peli4) ")
                if pelicula_elegida in self.peliculas:
                    index = list(self.peliculas.keys()).index(pelicula_elegida)
                    self.contadores_tikets[index] += 1
                    print(f"Ha adquirido un tiquete para {pelicula_elegida}.")
                    self.cupones += 1

            elif self.accfre == "3":
                print("Lista de comidas:")
                for comida, precio in self.alimentos.items():
                    print(f"{comida}: ${precio}")
                comida_elegida = input("¿Qué alimento desea? (alimento1, alimento2, alimento3, alimento4) ")
                if comida_elegida in self.alimentos:
                    index = list(self.alimentos.keys()).index(comida_elegida)
                    self.contadores_alimentos[index] += 1
                    print(f"Ha adquirido {comida_elegida}.")
                    self.cupones += 1

            elif self.accfre == "4":
                pelicula_reservada = input("¿Qué película desea reservar? (proxima1, proxima2, proxima3, proxima4) ")
                if pelicula_reservada in self.proximas_peliculas:
                    print(f"Ha reservado {pelicula_reservada}.")

        else:
            print("Credenciales incorrectas.")

    def menu_visitante(self):
        self.accfree = input("""
                ¿Qué desea hacer?
                1. Ver lista de películas
                2. Comprar tiquetes
                3. Comprar comidas
                """)

        if self.accfree == "1":
            print("Lista de películas:")
            for pelicula, hora in self.peliculas.items():
                print(f"{pelicula}: {hora}")

        elif self.accfree == "2":
            print("Lista de películas:")
            for pelicula, _ in self.peliculas.items():
                print(pelicula)
            pelicula_elegida = input("¿De qué película desea el tiquete? (peli1, peli2, peli3, peli4) ")
            if pelicula_elegida in self.peliculas:
                index = list(self.peliculas.keys()).index(pelicula_elegida)
                self.contadores_tikets[index] += 1
                print(f"Ha adquirido un tiquete para {pelicula_elegida}.")
                self.cupones += 1

        elif self.accfree == "3":
            print("Lista de comidas:")
            for comida, precio in self.alimentos.items():
                print(f"{comida}: ${precio}")
            comida_elegida = input("¿Qué alimento desea? (alimento1, alimento2, alimento3, alimento4) ")
            if comida_elegida in self.alimentos:
                index = list(self.alimentos.keys()).index(comida_elegida)
                self.contadores_alimentos[index] += 1
                print(f"Ha adquirido {comida_elegida}.")
                self.cupones += 1

    def admin(self):
        tiv = [self.contadores_tikets]
        tia = [self.contadores_alimentos]
        print("Tiquetes vendidos por película:")
        for pelicula, cantidad in zip(self.peliculas.keys(), self.contadores_tikets):
            print(f"{pelicula}: {cantidad} tiquetes vendidos")
        print("Comidas vendidas por tipo:")
        for comida, cantidad in zip(self.alimentos.keys(), self.contadores_alimentos):
            print(f"{comida}: {cantidad} unidades vendidas")


if __name__ == "__main__":
    cinema = Cinema()
