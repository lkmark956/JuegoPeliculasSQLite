import tkinter as tk
from tkinter import messagebox, simpledialog
from game.logic import MovieGameLogic
from db.database import ScoreDatabase

class MovieGuessingGameGUI:
    def __init__(self, master, logic, db):
        self.master = master
        self.logic = logic
        self.db = db
        master.title("Adivina la Película o Serie")
        master.configure(bg="#22223b")

        # Puntos iniciales
        self.points = 30

        # Etiqueta de puntos
        self.points_label = tk.Label(master, text=f"Puntos: {self.points}", bg="#4a4e69", fg="#f2e9e4", font=("Arial", 12, "bold"))
        self.points_label.pack(pady=5)

        # Área de pistas
        self.hint_label = tk.Label(master, text="Pista:", bg="#22223b", fg="#c9ada7", font=("Arial", 11, "bold"))
        self.hint_label.pack(pady=5)
        self.hint_text = tk.Text(master, height=2, width=40, state='disabled', bg="#f2e9e4", fg="#22223b", font=("Arial", 11))
        self.hint_text.pack(pady=5)

        # Entrada de respuesta
        self.answer_entry = tk.Entry(master, width=40, bg="#f2e9e4", fg="#22223b", font=("Arial", 11))
        self.answer_entry.pack(pady=5)

        # Botón para pedir pista
        self.hint_button = tk.Button(master, text="Pedir pista", command=self.ask_hint, bg="#9a8c98", fg="#22223b", font=("Arial", 11, "bold"), activebackground="#c9ada7")
        self.hint_button.pack(pady=5)

        # Botón para comprobar respuesta
        self.check_button = tk.Button(master, text="Comprobar respuesta", command=self.check_answer, bg="#9a8c98", fg="#22223b", font=("Arial", 11, "bold"), activebackground="#c9ada7")
        self.check_button.pack(pady=5)

        # Histórico de puntuaciones
        self.history_label = tk.Label(master, text="Histórico de puntuaciones:", bg="#22223b", fg="#c9ada7", font=("Arial", 11, "bold"))
        self.history_label.pack(pady=5)
        self.history_listbox = tk.Listbox(master, width=40, bg="#f2e9e4", fg="#22223b", font=("Arial", 10))
        self.history_listbox.pack(pady=5)
        self.update_history()
        
    def update_history(self):
        self.history_listbox.delete(0, tk.END)
        scores = self.db.get_scores()
        for username, score in scores:
            self.history_listbox.insert(tk.END, f"{username}: {score}")

    def ask_hint(self):
        # Obtener la siguiente pista de la lógica
        hint = self.logic.get_current_hint()
        # Mostrar la pista en el área de texto
        self.hint_text.config(state='normal')
        self.hint_text.delete('1.0', tk.END)
        self.hint_text.insert(tk.END, hint)
        self.hint_text.config(state='disabled')
        # Restar puntos
        self.points -= 1
        self.points_label.config(text=f"Puntos: {self.points}")

    def check_answer(self):
        answer = self.answer_entry.get()
        if self.logic.check_answer(answer):
            # Pedir nombre de usuario
            username = tk.simpledialog.askstring("Nombre de usuario", "Introduce tu nombre para guardar la puntuación:")
            if username:
                self.db.add_score(username, self.points)
                self.update_history()
            messagebox.showinfo("¡Correcto!", "¡Has acertado la película/serie!")
            self.logic.next_movie()
            self.logic.reset_hints()
            self.points = 30
            self.points_label.config(text=f"Puntos: {self.points}")
            self.hint_text.config(state='normal')
            self.hint_text.delete('1.0', tk.END)
            self.hint_text.config(state='disabled')
            self.answer_entry.delete(0, tk.END)
        else:
            messagebox.showerror("Incorrecto", "Respuesta incorrecta. ¡Intenta de nuevo!")

if __name__ == "__main__":
    root = tk.Tk()
    logic = MovieGameLogic()  # Suponiendo que no requiere parámetros
    db = ScoreDatabase("puntuaciones.db")  # Ruta de la base de datos
    app = MovieGuessingGameGUI(root, logic, db)
    root.mainloop()