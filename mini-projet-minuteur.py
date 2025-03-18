import time
import tkinter
import winsound
from tkinter import messagebox


class ApplicationMinuteur:
    def __init__(self, root):
        self.root = root
        self.root.title("Minuteur d'Intervalles")
        self.root.geometry("1000x600")  # Augmentation de la hauteur pour accueillir le chronomètre

        tkinter.Label(self.root, text="Bienvenue dans le minuteur d'intervalles pour entraînements personnalisables!",
                      font=("Times New Roman", 15, "bold")).pack()

        tkinter.Label(self.root, text="Nombre de séries:").pack()
        self.entrée_nombre_serie = tkinter.Entry(self.root, width=10, bg="lightgray", highlightthickness=2)
        self.entrée_nombre_serie.pack()

        tkinter.Label(self.root, text="Nombre d'exercices par série:").pack()
        self.entrée_nombre_exercice = tkinter.Entry(self.root, width=10, bg="lightgray", highlightthickness=2)
        self.entrée_nombre_exercice.pack()

        tkinter.Label(self.root, text="Temps de travail (en secondes):").pack()
        self.entrée_temps_travail = tkinter.Entry(self.root, width=10, bg="lightgray", highlightthickness=2)
        self.entrée_temps_travail.pack()

        tkinter.Label(self.root, text="Temps de repos entre les exercices (en secondes):").pack()
        self.entrée_temps_repos_exercice = tkinter.Entry(self.root, width=10, bg="lightgray", highlightthickness=2)
        self.entrée_temps_repos_exercice.pack()

        tkinter.Label(self.root, text="Temps de repos entre les series (en secondes):").pack()
        self.entrée_temps_repos_serie = tkinter.Entry(self.root, width=10, bg="lightgray", highlightthickness=2)
        self.entrée_temps_repos_serie.pack()

        self.bouton_demarrer = tkinter.Button(self.root, text="Démarrer", command=self.demarrer_minuteur, bg="#1D1E21",
                                              fg="white", height=1, width=15)
        self.bouton_demarrer.pack()


        tkinter.Label(text="\n\n").pack()
        self.label_temps_restant = tkinter.Label(self.root, text="", font=("Helvetica", 20, "bold"))
        self.label_temps_restant.pack()

        self.temps_restant = 0

    def demarrer_minuteur(self):
        try:
            nombre_serie = int(self.entrée_nombre_serie.get())
            nombre_exercice = int(self.entrée_nombre_exercice.get())
            temps_travail = int(self.entrée_temps_travail.get())
            temps_repos_exercice = int(self.entrée_temps_repos_exercice.get())
            temps_repos_serie = int(self.entrée_temps_repos_serie.get())
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier pour la durée.")
            return

        self.bouton_demarrer.config(state=tkinter.DISABLED, bg="gray")

        for serie in range(1, nombre_serie + 1):
            for exercice in range(1, nombre_exercice + 1):
                winsound.Beep(400, 700)
                self.root.update()  # Rafraîchissement de l'interface graphique
                self.minuteur(temps_travail, "Série {}, Exercice {}: ".format(serie, exercice))
                if exercice != nombre_exercice:
                    winsound.Beep(700, 700)
                    self.root.update()
                    self.minuteur(temps_repos_exercice, "REPOS entre exercices: ")
            if serie != nombre_serie:
                winsound.Beep(700, 700)
                self.root.update()
                self.minuteur(temps_repos_serie, "REPOS entre séries: ")

        messagebox.showinfo("FIN", "bien jouer vous avez terminer votre entrainement")
        self.bouton_demarrer.config(state=tkinter.NORMAL, bg="#1D1E21")
    def minuteur(self, duree=0, message=""):
        self.temps_restant = duree
        while self.temps_restant > 0:
            minutes = self.temps_restant // 60
            secondes = self.temps_restant % 60
            temps_format = "{:02d}:{:02d}".format(minutes, secondes)
            self.label_temps_restant.config(text=message + "  " + temps_format , bg="lightblue")
            self.root.update()
            time.sleep(1)
            self.temps_restant -= 1


if __name__ == "__main__":
    root = tkinter.Tk()
    app = ApplicationMinuteur(root)
    root.mainloop()
