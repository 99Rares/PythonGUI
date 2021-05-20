import tkinter as tk
from tkinter import messagebox

from Benutzer_Class import Benutzer
from Film_Class import Film
from Pages import Page


# noinspection PyShadowingBuiltins,PyUnboundLocalVariable
class GemeinsamesWindow(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.__benutzer = []
        self.__filme = []
        self.inputData()
        # Film Title
        self.__ben_name = tk.StringVar()
        label_ben_name = tk.Label(self, text="Benutzer Name: ", font='bold,14', pady=10)
        label_ben_name.grid(row=0, column=0)
        film_name_entry = tk.Entry(self, textvariable=self.__ben_name)
        film_name_entry.grid(row=0, column=1)

        # Film Jahr
        self.__bestell = tk.StringVar()
        label_bestell = tk.Label(self, text="Bestellung: ", font='bold,14', pady=10)
        label_bestell.grid(row=1, column=0)
        bestell_entry = tk.Entry(self, textvariable=self.__bestell)
        bestell_entry.grid(row=1, column=1)

        # Film Wertung
        self.__film_wertung = tk.StringVar()
        label_film_wertung = tk.Label(self, text="Wertung: ", font='bold,14', pady=10)
        label_film_wertung.grid(row=2, column=0)
        film_wertung_entry = tk.Entry(self, textvariable=self.__film_wertung)
        film_wertung_entry.grid(row=2, column=1)

        # Film sch
        self.__film_schauspieler = tk.StringVar()
        label_film_schauspieler = tk.Label(self, text="Schauspieler: ", font='bold,14', pady=10)
        label_film_schauspieler.grid(row=4, column=0)
        film_schauspieler_entry = tk.Entry(self, textvariable=self.__film_schauspieler)
        film_schauspieler_entry.grid(row=4, column=1)

        # Button
        print_btn = tk.Button(self, text='Benutzer Anzeigen', command=self.printItem)
        print_btn.grid(row=1, column=3)

        add_btn = tk.Button(self, text='Anzeigen Schauspiller', command=self.addItem)
        add_btn.grid(row=0, column=3, pady=20, padx=50)

        update_btn = tk.Button(self, text='Anzeigen Filme Wertung', command=self.updateItem)
        update_btn.grid(row=2, column=3)

        clear_btn = tk.Button(self, text='Bestellen', command=self.clearItem)
        clear_btn.grid(row=4, column=3)

        save_btn = tk.Button(self, text='Save', command=self.save)
        save_btn.grid(row=5, column=3,pady=10)

        help_btn =tk.Button(self, text='Help', command=self.help)
        help_btn.grid(row=6, column=3,pady=10)

    def anzeigeBenutzer(self):
        ben = ''
        print("Die Liste von Benutzer:")
        for i in self.__benutzer:
            ben = ben + i.get_v_name() + ' ' + i.get_name() + '\n' + str(i.get_bestell()) + '\n'
            ben=ben+'Summe Bestllung: '+str(self.getSUM(i.get_v_name()))+'\n\n'
        return ben

    def addBenutzer_Txt(self, data):
        """
        Liest aus die gelesen Daten
        """
        for benutzer in data:
            benutzer = benutzer.replace('\n', '').split(',')
            benutzer[2] = benutzer[2].split(";")
            self.__benutzer.append(Benutzer(benutzer[0], benutzer[1], benutzer[2]))

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

    def inputBenData(self):
        """
        Liest aus ein Datei
        """
        benutzer = open("Benutzer.txt", 'r')
        benData = benutzer.readlines()
        self.addBenutzer_Txt(benData)

    def inputFilmData(self):
        """
        Liest aus ein Datei
        """
        filme = open("Filme.txt", 'r')
        filmData = filme.readlines()

        self.addFilme_Txt(filmData)

    def inputData(self):
        """
        Liest aus ein Datei
        """
        self.inputBenData()
        self.inputFilmData()

    def bestimteSchauspieler(self, schauspieler):
        sch = schauspieler + " hat in den folgenden Filme gespielt: \n"
        for film in self.__filme:
            if film.hatSchauspieler(schauspieler):
                sch = sch + film.getTitel() + '\n'
        return sch

    def benutzer_finden(self, name):
        print(name)
        id_ben = 0
        for i in self.__benutzer:
            print(i.get_v_name())
            if i.get_v_name() == name:
                return id_ben
            id_ben += 1
        return -1

    def getSUM(self, benutzer):
        """
        Gesamter Preis von alle Bestellungen.
        """
        ID = self.benutzer_finden(benutzer)
        preis = 0
        preis += self.getPreis(self.__benutzer[ID].get_bestell())
        return preis

    def getPreis(self, bestellung):
        """
        Get Bestellung Preis
        """
        preis = 0
        for i in bestellung:
            ID = self.filme_finden(i)
            if ID != None:
                preis += self.__filme[ID].getPreis()
        return preis

    def filme_finden(self, titel):
        id_film = 0
        for i in self.__filme:
            if i.getTitel() == titel:
                return id_film
            id_film += 1
        return None

    def film_note(self, note):
        wert = "Filme mit wertung grosser als" + str(note) + ':\n '
        print("Filme mit wertung grosser als:" + str(note))
        for film in self.__filme:
            if film.getWertung() > note:
                wert = wert + film.getTitel() + '\n'
        return wert

    def bestellen(self, benutzer, bestellung):
        """
        Fugt eine Bestellung hinzu
        """
        ID = self.benutzer_finden(benutzer)
        if ID==-1:
            ID=None
        else:
            pass
        try:
            self.__benutzer[ID].set_bestell(bestellung)
            print(("Update durchgefugt", 'blue'))
        except:
            print(("Update NICHT durchgefugt", 'red'))

    def outputBenutzerData(self):
        """
        Speichert Data in Benutzer.txt
        """
        out = open("Benutzer.txt", "w")
        for benutzer in self.__benutzer:
            bestellungen = ""
            for bestellung in benutzer.get_bestell():
                for film in bestellung:
                    bestellungen += film
                bestellungen += ';'
            bestellungen = bestellungen[:-1]
            line = benutzer.get_v_name() + "," + benutzer.get_name() + "," + bestellungen + '\n'
            out.write(line)
        out.close()

    def addItem(self):
        messagebox.showinfo("Acrots", self.bestimteSchauspieler(self.__film_schauspieler.get()))
        print("ok")

    def printItem(self):
        messagebox.showinfo("Verfugbare Filme", self.anzeigeBenutzer())
        print('Delete')

    def updateItem(self):
        try:
            messagebox.showinfo("", self.film_note(float(self.__film_wertung.get())))
        except:
            pass
        print('Update')

    def clearItem(self):
        film = 'film'
        bestelle = []
        if film != '':
            print('Um zu beenden drucken geben sie nichts ein (einfach "ENTER" drucken)')
            film = self.__bestell.get()
            bestelle.append(film + ';')
            print(bestelle)
        self.bestellen(self.__ben_name.get(),bestelle)
        print('Clear')

    def save(self):
        print('save')
        self.outputBenutzerData()

    def help(self):
        help_pls = "Der Knopf 'Anzeigen Schauspiller' zeigt in welchen Filme ein Schauspiller gespielt hat(" \
                  "Schauspieler wehlen)\n"+"Der Knopf 'Benuzer anzeigen' zeigt die existierende Benutzern mit ihre " \
                  "Bestellung \n"+"Der Knopf 'Wertung Anzeigen' zeigt welche Filme den Rating grosser als etwas " \
                  "haben(Raring wehlen)\n"+"Das Knopf 'Bestellen' fugt ein Film zu einer Bestellung\n"+"Das Knoplf " \
                  "'Save'speigert in der Datei "
        messagebox.showinfo("Help",help_pls)
