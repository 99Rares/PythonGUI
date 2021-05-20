from termcolor import colored

from gem import Gemeinsam as gem


class BigMenu:
    def __init__(self):
        self.menu = gem()

    @staticmethod
    def meniu4():
        """
        Die Funktion schreibt die optionen auf dem Bildschirm

        """
        try:
            print(colored("""
        1. Benutzer
        2. Filme
        3. Gemeinsames
        4. Exit
                    """, 'green'))
        except Exception as e:
            print(str(e))

    def main_menu(self):
        # Main menu
        key = True
        self.meniu4()
        while key:

            key = input("Wahle ein meniu: ")
            if key == "1":
                self.menu_benutzer()
                self.meniu4()

            elif key == "2":
                self.film_menu()
                self.meniu4()

            elif key == "3":
                self.meniu_gem()
                self.meniu4()

            elif key == "4":
                print(colored("Goodbye!", 'blue'))
                self.Tests()
                self.menu.outputData()
                key = False

        exit()

    @staticmethod
    def meniu1():
        """
        Zeigt den Menu an
        """
        try:
            print(colored("""
        1.Einfugen
        2.Wachseln des Nachnamens
        3.Loschen
        4.Main meniu
                    """, 'green'))
        except Exception as e:
            print(str(e))

    def menu_benutzer(self):
        """
        Die Funktion kontroliert den Menu.

        """

        try:
            self.meniu1()
            key = True
            while key:
                key = int(input("Wahle eine Funktion: "))
                if key == 1:
                    v_name = input('Vorname: ')
                    name = input('Nachname: ')
                    self.menu.einfugenBen(v_name, name)
                    self.meniu1()
                elif key == 2:
                    name = input("Vorname eingeben: ")
                    newName = input("New Nachname: ")
                    self.menu.updateName(name, newName)
                    self.meniu1()
                elif key == 3:
                    name = input('Vorname eingeben: ')
                    self.menu.del_ben(name)
                    self.meniu1()
                elif key == 4:
                    self.meniu1()
                    key = False

        except Exception as e:
            print(str(e))

    @staticmethod
    def meniu2():
        """
        Zeigt den Menu an
        """
        try:
            print(colored("""
        1.Einfugen
        2.Preis Akutalisierung
        3.Anzeige der Filme
        4.Main meniu
            """, "green"))
        except Exception as e:
            print(str(e))

    def film_menu(self):
        """
        Die Funktion kontroliert den Menu.
        """

        try:
            self.meniu2()
            key = True
            while key:
                key = int(input("Wahle eine Funktion: "))
                if key == 4:
                    key = False
                elif key == 1:
                    titel = input("Titel: ")
                    jahr = int(input("Jahr: "))
                    wertung = float(input("Wertung: "))
                    schauspieler = input("Schauspieler: ").split(", ")
                    preis = float(input("Preis: "))
                    self.menu.einfugenFilm(titel, jahr, wertung, schauspieler, preis)
                    self.meniu2()
                elif key == 2:
                    titel = input("Titel des Films: ")
                    preis = int(input("Neues Preis: "))
                    self.menu.updatePreis(titel, preis)
                    self.meniu2()
                elif key == 3:
                    self.menu.anzeigeFilme()
                    self.meniu2()
        except Exception as e:
            print(str(e))

    @staticmethod
    def meniu3():
        """
            Zeigt den Menu an
            """
        try:
            print(colored("""
            1. Preis einer Bestellung
            2. Neue Bestellung
            3. Anzeige ratings
            4. Anzeige Filme mit bestimmten Schauspierler
            5. Anzeige Benutzern
            6. Main meniu
                        """, 'green'))
        except Exception as e:
            print(str(e))

    def meniu_gem(self):
        key = True
        self.meniu3()
        while key:
            key = input("Wahle eine Funktion:\n ")

            if key == "1":
                print("Preis welcher Bestellung willst du sehen:")
                self.menu.anzeigeBenutzer()
                v_name = input("Geben Sie den Vornamen ein : ")
                x = self.menu.getSUM(v_name)
                if x > 0:
                    print(x)
                self.meniu3()

            elif key == "2":
                print('Wer will bestellen?')
                self.menu.anzeigeBenutzer()
                name = input("Geben Sie den Vornamen ein : ")
                film = 'film'
                bestelle = []
                while film != '':
                    print('Um zu beenden drucken geben sie nichts ein (einfach "ENTER" drucken)')
                    film = input("Name des Films: ")
                    bestelle.append(film + ';')
                    print(bestelle)
                self.menu.bestellen(name, bestelle)
                self.meniu3()

            elif key == "3":
                rating = float(input("Gib ein Rating: "))
                self.menu.film_note(rating)
                self.meniu3()

            elif key == "4":
                actor = input("Gib ein Schauspieler: ")
                self.menu.bestimteSchauspieler(actor)
                self.meniu3()

            elif key == "5":
                print('Anzeige Benutzer')
                self.menu.anzeigeBenutzer()
                self.meniu3()

            elif key == "6":
                key = False

            else:
                print(colored("Gib eine valide Zahl", "red"))

    def Tests(self):
        try:
            # self.menu.einfugenFilm('aaa', 1234, 1, ['a', 'b', 'c'], 2)
            assert self.menu.getSUM('Rares') == 179
            assert self.menu.benutzer_finden('Rares') == 0
            assert self.menu.filme_finden('Star-Wars_IV') == 0
            b = ['Transformers', 'Transformers', 'The Dark Knight','Star-Wars_IV']
            assert self.menu.getPreis(b) == 75
        except AssertionError:
            print(AssertionError)

    def main_start(self):
        self.menu.inputData()
        self.main_menu()
