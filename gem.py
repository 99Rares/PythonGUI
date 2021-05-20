from termcolor import colored
from Benutzer_Class import Benutzer
from Film_Class import Film


class Gemeinsam:
    """
    Diese Klasse enthalt Funktionen fur die Verwaltung des Shops.

    Attributes: benutzer, filme
    """

    def __init__(self):
        self.__benutzer = []
        self.__filme = []

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

    def outputData(self):
        print("aici")
        """
         Speichert Data in Film.txt und Benutzer.txt
        """
        self.outputBenutzerData()
        self.outputFilmeData()

    def benutzer_finden(self, name):
        id_ben = 0
        for i in self.__benutzer:
            if i.get_v_name() == name:
                return id_ben
            id_ben += 1
        return -1

    def filme_finden(self, titel):
        id_film = 0
        for i in self.__filme:
            if i.getTitel() == titel:
                return id_film
            id_film += 1
        return None

    def einfugenBen(self, v_name, name):
        """
        Erstellt ein Benutzer
        """
        self.__benutzer.append(Benutzer(v_name, name))
        print(colored("Benutzer wurde eingefugt", 'blue'))

    def einfugenFilm(self, titel, jahr, wertung, schauspieler, preis):
        """
        Erstellt ein Film
        """
        self.__filme.append(Film(titel, jahr, wertung, schauspieler, preis))
        print(colored("Film wurde eingefugt", 'blue'))

    def updateName(self, oldName, newName):
        """
        aktualisiert den Nachnamen
        """
        ID = self.benutzer_finden(oldName)
        if ID == -1:
            pass
        else:
            ID = 'False'
        try:

            self.__benutzer[ID].set_name(newName)
            print(colored("Update durchgefugt", 'blue'))
        except:
            print(colored("Update NICHT durchgefugt", 'red'))

    def updatePreis(self, titel, neuePreis):
        """
        Andert die Preis eines Film.
        """
        ID = self.filme_finden(titel)
        if ID==-1:
            ID = 'None'
        else:
            pass
        try:
            self.__filme[ID].setPreis(neuePreis)
            print(colored("Update durchgefugt", 'blue'))
        except:
            print(colored("Update NICHT durchgefugt", 'red'))

    def del_ben(self, name):
        """
        Loscht ein Benutzer
        """
        ID = self.benutzer_finden(name)
        if ID==-1:
            pass
        else:
            ID = 'False'
        try:
            del self.__benutzer[ID]
            print(colored("Loschung durchgefugt", 'blue'))
        except:
            print(colored("Loschung NICHT durchgefugt", 'red'))

    def anzeigeBenutzer(self):
        print("Die Liste von Benutzer:")
        for i in self.__benutzer:
            i.print_Ben()

    def anzeigeFilme(self):
        print("Die Liste von Filme:")
        for i in self.__filme:
            i.print_filme()

    def bestellen(self, benutzer, bestellung):
        """
        Fugt eine Bestellung hinzu
        """
        ID = self.benutzer_finden(benutzer)
        if ID==-1:
            pass
        else:
            ID = 'False'
        try:
            self.__benutzer[ID].set_bestell(bestellung)
            print(colored("Update durchgefugt", 'blue'))
        except:
            print(colored("Update NICHT durchgefugt", 'red'))

    def getPreis(self, bestellung):
        """
        Get Bestellung Preis
        """
        preis = 0
        for i in bestellung:
            ID = self.filme_finden(i)
            if ID != -1:
                preis += self.__filme[ID].getPreis()
        return preis

    def printUser(self):
        print("Die Liste von Benutzer mit aktuelle Bestellungen: ")
        for i in self.__benutzer:
            i.print_Ben()

    def film_note(self, note):
        print("Filme mit wertung grosser als:" + str(note))
        for film in self.__filme:
            if film.getWertung() > note:
                print(film.getTitel())

    def bestimteSchauspieler(self, schauspieler):
        print(schauspieler + " hat in den folgenden Filme gespielt: ")
        for film in self.__filme:
            if film.hatSchauspieler(schauspieler):
                print(film.getTitel())

    def getSUM(self, benutzer):
        """
        Gesamter Preis von alle Bestellungen.
        """
        ID = self.benutzer_finden(benutzer)
        preis = 0
        preis += self.getPreis(self.__benutzer[ID].get_bestell())
        return preis
