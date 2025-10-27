import tkinter as tk
from gui.interface import MovieGuessingGameGUI
from game.logic import MovieGameLogic
from db.database import ScoreDatabase

if __name__ == "__main__":
    root = tk.Tk()
    logic = MovieGameLogic()
    db = ScoreDatabase()
    app = MovieGuessingGameGUI(root, logic, db)
    root.mainloop()
    db.close()