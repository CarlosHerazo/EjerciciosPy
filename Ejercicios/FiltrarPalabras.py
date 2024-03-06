class FiltroPalabras:
    def __init__(self):
        self.palabras = []

    def ingresar_palabras(self):
        try:
            input_palabras = input("Ingrese palabras separadas por espacios: ")
            self.palabras = input_palabras.split()
        except ValueError:
            print(
                "Error al ingresar las palabras. recuerda los espacios"
            )

    def filtrar_pal(self, n):
        new_palabras = [palabra for palabra in self.palabras if len(palabra) > n]
        return new_palabras


try:
    filtro = FiltroPalabras()
    filtro.ingresar_palabras()
    n_caracteres = int(input("Ingrese el numero de caracteres para filtrar: "))
    resultado = filtro.filtrar_pal(n_caracteres)
    print("Palabras filtradas:", resultado)
except ValueError:
    print(
        "Error al ingresar el numero minimo de caracteres. Asegurese de ingresar un valor numerico."
    )
