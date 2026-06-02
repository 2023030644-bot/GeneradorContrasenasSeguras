import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class GeneradorPasswords:

    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Contraseñas Seguras")
        self.root.geometry("650x450")
        self.root.resizable(False, False)

        titulo = tk.Label(
            root,
            text="Generador de Contraseñas Seguras",
            font=("Arial", 20, "bold")
        )
        titulo.pack(pady=15)

        descripcion = tk.Label(
            root,
            text="Programa basado en las buenas prácticas de seguridad informática",
            font=("Arial", 10)
        )
        descripcion.pack()

        frame = tk.Frame(root)
        frame.pack(pady=20)

        tk.Label(
            frame,
            text="Longitud:"
        ).grid(row=0, column=0, padx=10)

        self.longitud = tk.Entry(frame, width=10)
        self.longitud.insert(0, "16")
        self.longitud.grid(row=0, column=1)

        self.mayusculas = tk.BooleanVar(value=True)
        self.minusculas = tk.BooleanVar(value=True)
        self.numeros = tk.BooleanVar(value=True)
        self.simbolos = tk.BooleanVar(value=True)

        ttk.Checkbutton(
            root,
            text="Incluir mayúsculas",
            variable=self.mayusculas
        ).pack()

        ttk.Checkbutton(
            root,
            text="Incluir minúsculas",
            variable=self.minusculas
        ).pack()

        ttk.Checkbutton(
            root,
            text="Incluir números",
            variable=self.numeros
        ).pack()

        ttk.Checkbutton(
            root,
            text="Incluir símbolos",
            variable=self.simbolos
        ).pack()

        ttk.Button(
            root,
            text="Generar Contraseña",
            command=self.generar
        ).pack(pady=20)

        self.resultado = tk.Entry(
            root,
            width=50,
            font=("Consolas", 14),
            justify="center"
        )
        self.resultado.pack(pady=10)

        ttk.Button(
            root,
            text="Copiar",
            command=self.copiar
        ).pack()

        self.estado = tk.Label(
            root,
            text="",
            fg="green"
        )
        self.estado.pack(pady=15)

    def generar(self):

        try:
            longitud = int(self.longitud.get())

            if longitud < 12:
                messagebox.showwarning(
                    "Advertencia",
                    "La longitud mínima recomendada es 12."
                )
                return

            caracteres = ""

            if self.mayusculas.get():
                caracteres += string.ascii_uppercase

            if self.minusculas.get():
                caracteres += string.ascii_lowercase

            if self.numeros.get():
                caracteres += string.digits

            if self.simbolos.get():
                caracteres += "!@#$%^&*()_+-=?"

            if caracteres == "":
                messagebox.showerror(
                    "Error",
                    "Selecciona al menos un tipo de carácter."
                )
                return

            password = "".join(
                random.choice(caracteres)
                for _ in range(longitud)
            )

            self.resultado.delete(0, tk.END)
            self.resultado.insert(0, password)

            self.estado.config(
                text="Contraseña generada correctamente"
            )

        except ValueError:
            messagebox.showerror(
                "Error",
                "Ingresa una longitud válida."
            )

    def copiar(self):
        password = self.resultado.get()

        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)

            self.estado.config(
                text="Contraseña copiada al portapapeles"
            )

root = tk.Tk()
app = GeneradorPasswords(root)
root.mainloop()