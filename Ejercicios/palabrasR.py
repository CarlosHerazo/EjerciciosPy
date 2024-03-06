class FiltroPalabras:
    def __init__(self):
        self.palabras = []

    def ingresar_palabras(self):
        try:
            input_palabras = input("Ingrese palabras separadas por espacio: ")
            self.palabras = input_palabras.split()
        except ValueError:
            print(
                "Error al ingresar las palabras. Asegúrese de ingresar palabras separadas por espacio."
            )

    def filtrar_palabras(self, n):
        palabras_filtradas = [palabra for palabra in self.palabras if len(palabra) > n]
        return palabras_filtradas


try:
    filtro = FiltroPalabras()
    filtro.ingresar_palabras()
    n_caracteres = int(input("Ingrese el número mínimo de caracteres para filtrar: "))
    resultado = filtro.filtrar_palabras(n_caracteres)
    print("Palabras filtradas:", resultado)
except ValueError:
    print(
        "Error al ingresar el número mínimo de caracteres. Asegúrese de ingresar un valor numérico."
    )
