from prettytable import PrettyTable


class BibliotecaN:
    def __init__(self):
        self.listaLibros = {
            "Titulo del Libro": [
                "Cien años de soledad",
                "Rayuela",
                "La tia Julia y el escribidor",
            ],
            "Autor": [
                "Gabriel García Marquez",
                "Mario Vargas Llosa",
                "Julio Corteza",
            ],
            "Año": [
                "1977",
                "1963",
                "1967",
            ],
            "Editorial": [
                "Sudamerica",
                "Sudamerica",
                "Seix Barral",
            ],
            "Ref. Bibliografia": [
                "857.67/M566",
                "863.55/J5667",
                "868.23/L567",
            ],
        }


class Biblioteca(BibliotecaN):
    def __init__(self, nombre):
        super().__init__()
        self.listaLibrosB = self.listaLibros
        self.nombre = nombre
        self.tabla = PrettyTable()
        # print(self.listaLibrosB)

    def _agregarLibros(self, titulo, autor, year, editorial, ref):
        try:
            # así se agregan elementos a una lista que estan dentro de un diccionario
            self.listaLibrosB["Titulo del Libro"].append(titulo)
            self.listaLibrosB["Autor"].append(autor)
            self.listaLibrosB["Año"].append(year)
            self.listaLibrosB["Editorial"].append(editorial)
            self.listaLibrosB["Ref. Bibliografia"].append(ref)

            return print(f"El libro {titulo} fue agregado exitosamente")
        except:
            return print("Algo salio mal al intentar agregar el libro")

    def _listarLibros(self):

        self.tabla.clear()  # Reiniciar la tabla para evitar duplicados

        # agregamos las columnas
        columnas = list(self.listaLibrosB.keys())
        self.tabla.field_names = columnas

        # agregamos las filas
        for i in range(len(self.listaLibrosB[columnas[0]])):
            fila = [self.listaLibrosB[columna][i] for columna in columnas]         
            self.tabla.add_row(fila)

        return print(self.tabla)
