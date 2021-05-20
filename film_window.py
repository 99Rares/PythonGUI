import tkinter as tk
from tkinter import messagebox

from Pages import Page
from Film_Class import Film


# noinspection PyShadowingBuiltins
class FilmWindow(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.__filme = []
        self.inputFilmData()
        # Film Title
        self.__film_name = tk.StringVar()
        label_film_name = tk.Label(self, text="Film Name: ", font='bold,14', pady=10)
        label_film_name.grid(row=0, column=0)
        film_name_entry = tk.Entry(self, textvariable=self.__film_name)
        film_name_entry.grid(row=0, column=1)

        # Film Jahr
        self.__film_jahr = tk.StringVar()
        label_film_jahr = tk.Label(self, text="Jahr: ", font='bold,14', pady=10)
        label_film_jahr.grid(row=1, column=0)
        film_jahr_entry = tk.Entry(self, textvariable=self.__film_jahr)
        film_jahr_entry.grid(row=1, column=1)

        # Film Wertung
        self.__film_wertung = tk.StringVar()
        label_film_wertung = tk.Label(self, text="Wertung: ", font='bold,14', pady=10)
        label_film_wertung.grid(row=2, column=0)
        film_wertung_entry = tk.Entry(self, textvariable=self.__film_wertung)
        film_wertung_entry.grid(row=2, column=1)

        # Film Preis
        self.__film_preis = tk.StringVar()
        label_film_preis = tk.Label(self, text="Preis: ", font='bold,14', pady=10)
        label_film_preis.grid(row=3, column=0)
        film_preis_entry = tk.Entry(self, textvariable=self.__film_preis)
        film_preis_entry.grid(row=3, column=1)

        # Film sch
        self.__film_schauspieler = tk.StringVar()
        label_film_schauspieler = tk.Label(self, text="Schauspieler: ", font='bold,14', pady=10)
        label_film_schauspieler.grid(row=4, column=0)
        film_schauspieler_entry = tk.Entry(self, textvariable=self.__film_schauspieler)
        film_schauspieler_entry.grid(row=4, column=1)

        # Button
        print_btn = tk.Button(self, text='Filme Anzeigen', command=self.printItem)
        print_btn.grid(row=1, column=3)

        add_btn = tk.Button(self, text='Add Film', command=self.addItem)
        add_btn.grid(row=0, column=3, pady=20, padx=50)

        update_btn = tk.Button(self, text='Update Film', command=self.updateItem)
        update_btn.grid(row=2, column=3)

        save_btn = tk.Button(self, text='Save', command=self.save)
        save_btn.grid(row=3, column=3)

        help_btn = tk.Button(self, text='Help', command=self.help)
        help_btn.grid(row=4, column=3, pady=10)

    def addFilme_Txt(self, data):
        """
        Liest aus die gelesen Daten
        """
        for film in data:
            film = film.replace('\n', '').split(',')
            film[1] = int(film[1])
            film[2] = float(film[2])
            film[4] = float(film[4])
            film[3] = film[3].split(';')
            self.__filme.append(Film(film[0], film[1], film[2], film[3], film[4]))
            print('ok')

    def inputFilmData(self):
        """
        Liest aus ein Datei
        """
        filme = open("Filme.txt", 'r')
        filmData = filme.readlines()

        self.addFilme_Txt(filmData)

    def outputFilmeData(self):
        """
        Speichert Data in Film.txt
        """
        out = open("Filme.txt", "w")
        for film in self.__filme:
            schauspielerList = ""
            for sch in film.getSchauspieler():
                schauspielerList += sch + ';'
            schauspielerList = schauspielerList[:-1]
            line = film.getTitel() + ',' + str(film.getJahr()) + ',' + str(film.getWertung()) + ',' + \
                   schauspielerList + ',' + str(film.getPreis()) + '\n'
            out.write(line)
        out.close()

    def updatePreis(self, titel, neuePreis):
        """
        Andert die Preis eines Film.
        """
        print(titel)
        print(neuePreis)
        ID = self.filme_finden(titel)

        if ID == -1:
            ID = 'None'
        else:
            pass
        try:
            self.__filme[ID].setPreis(neuePreis)
            print(("Update durchgefugt", 'blue'))
        except:
            print(("Update NICHT durchgefugt", 'red'))

    def filme_finden(self, titel):
        id_film = 0
        for i in self.__filme:
            if i.getTitel() == titel:
                return id_film
            id_film += 1
        return None

    def anzeigeFilme(self):
        film = ''
        print("Die Liste von Filme:")
        for i in self.__filme:
            film = film + i.getTitel() + '\n'
        return film

    def addItem(self):
        try:
            name = self.__film_name.get()
            jahr = int(self.__film_jahr.get())
            wert = float(self.__film_wertung.get())
            preis = float(self.__film_preis.get())
            schauspieler = self.__film_schauspieler.get()
            schauspieler = schauspieler.split(',')
            new_Film = Film(name, jahr, wert, schauspieler, preis)
            self.__filme.append(new_Film)
        except ValueError as e:
            print(e)
        messagebox.showinfo("Info", "Film eingefuhrt")

    def printItem(self):
        messagebox.showinfo("Verfugbare Filme", self.anzeigeFilme())
        print('Delete')

    def updateItem(self):
        self.updatePreis(self.__film_name.get(), int(self.__film_preis.get()))
        messagebox.showinfo("", "Update durchgefuhrt")
        print('Update')

    def clearItem(self):
        print('Clear')

    def save(self):
        print('save')
        self.outputFilmeData()

    def help(self):
        help_pls = "Der Knopf 'Add Film' fugt ein Film hinzu(Parameter wehlen)\n" + "Der Knopf 'Filme " \
                                                                                    "Anzeigen' zeigt die Filme an\n" + "Der Knopf ' Update Film' " \
                                                                                                                       "aktualisiert den Preis des Films(Name und Preis wehlen)\n" \
                   + "Das Knoplf 'Save'speigert in der Datei "
        messagebox.showinfo("Help", help_pls)
