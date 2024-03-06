"""


"""

import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfMerger
import os


class Unirpdf:
    def __init__(self):
        # Llama al metodo para seleccionar archivos PDF
        self.pdf_files = self.select_pdfs()
        # Si se han seleccionado archivos PDF, realiza la unión
        if self.pdf_files:
            self.union_pdfs()
            

    def select_pdfs(self):
        # Configura la int  erfaz grafica de seleccion de archivos
        root = tk.Tk()
        root.withdraw()  # Oculta la ventana principal

        # Muestra el cuadro de diálogo para seleccionar archivos PDF
        file_paths = filedialog.askopenfilenames( 
            title="Seleccionar archivos PDF",
            filetypes=[("Archivos PDF", "*.pdf"), ("Todos los archivos", "*.*")],
        )

        # Devuelve la lista de rutas de archivos seleccionados
        return file_paths

    def union_pdfs(self):
        # Verifica si hay archivos PDF seleccionados
        if self.pdf_files:
            # Obtiene la ruta completa para guardar el archivo PDF unido
            desktop_path = os.path.join(
                os.getenv("USERPROFILE"), "OneDrive", "Escritorio"
            )
            output_filename = os.path.join(desktop_path, "docFinally.pdf")

            # Crea una instancia de PdfMerger
            merger = PdfMerger()

            # Itera sobre los archivos PDF seleccionados y los fusiona
            for pdf in self.pdf_files:
                merger.append(open(pdf, "rb"))

            # Guarda el archivo PDF unido en la ruta especificada
            with open(output_filename, "wb") as output_file:
                merger.write(output_file)

            print(f"PDFs unidos correctamente en {output_filename}")


unirpdf_instance = Unirpdf()
