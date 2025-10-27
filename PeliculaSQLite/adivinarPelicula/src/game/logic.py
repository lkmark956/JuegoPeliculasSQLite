class MovieGameLogic:
    def __init__(self):
        # Ejemplo de películas y pistas (sin series)
        self.movies = [
            {
                "title": "Titanic",
                "hints": [
                    "Es una película romántica y dramática.",
                    "Fue dirigida por James Cameron.",
                    "El barco se hunde.",
                    "Protagonizada por Leonardo DiCaprio y Kate Winslet."
                ]
            },
            {
                "title": "El Padrino",
                "hints": [
                    "Película de la mafia.",
                    "Dirigida por Francis Ford Coppola.",
                    "Protagonizada por Marlon Brando y Al Pacino.",
                    "La familia Corleone."
                ]
            },
            {
                "title": "Forrest Gump",
                "hints": [
                    "El protagonista corre mucho.",
                    "Su madre le dice que la vida es como una caja de bombones.",
                    "Protagonizada por Tom Hanks.",
                    "Tiene una relación especial con Jenny."
                ]
            },
            {
                "title": "Jurassic Park",
                "hints": [
                    "Dinosaurios en una isla.",
                    "Dirigida por Steven Spielberg.",
                    "Un parque temático peligroso.",
                    "El T-Rex escapa."
                ]
            },
            {
                "title": "La La Land",
                "hints": [
                    "Musical romántico.",
                    "Protagonizada por Emma Stone y Ryan Gosling.",
                    "Ambientada en Los Ángeles.",
                    "La música y el baile son clave."
                ]
            },
            {
                "title": "Gladiator",
                "hints": [
                    "Ambientada en la antigua Roma.",
                    "Protagonizada por Russell Crowe.",
                    "El protagonista busca venganza.",
                    "Famosa por la frase '¿Estáis entretenidos?'"
                ]
            },
            {
                "title": "Matrix",
                "hints": [
                    "Realidad simulada.",
                    "Protagonizada por Keanu Reeves.",
                    "Pastilla roja o azul.",
                    "Dirigida por las hermanas Wachowski."
                ]
            },
            {
                "title": "Avatar",
                "hints": [
                    "Planeta Pandora.",
                    "Dirigida por James Cameron.",
                    "Protagonizada por Sam Worthington y Zoe Saldana.",
                    "Seres azules llamados Na'vi."
                ]
            }
        ]
        self.current_index = 0
        self.hint_index = 0

    def get_current_hint(self):
        if self.hint_index < len(self.movies[self.current_index]["hints"]):
            hint = self.movies[self.current_index]["hints"][self.hint_index]
            self.hint_index += 1
            return hint
        else:
            return "No hay más pistas disponibles."

    def check_answer(self, answer):
        correct = self.movies[self.current_index]["title"].lower() == answer.strip().lower()
        return correct

    def next_movie(self):
        self.current_index = (self.current_index + 1) % len(self.movies)
        self.hint_index = 0

    def reset_hints(self):
        self.hint_index = 0