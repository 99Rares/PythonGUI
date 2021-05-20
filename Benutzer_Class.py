class Benutzer:
    """
        Die Klasse ist fur die Users des Online Shops.
        Die Klasse enthalt: den Konstruktor und get und set Funktionen fur alle Attribute.

        Attribute des Konstruktors:
            Vorname (string), Nachname (string), Bestellungen (list)
        """

    def __init__(self, vorname, nachname, bestell=[]):
        """
        Der Konstruktor der Klasse.

        Parameters:
            Vorname (string), Nachname (string)
        """
        self.__Vorname = vorname
        self.__Nachname = nachname
        self.__bestellungen = bestell

    def __str__(self):
        bestellungen = ""
        for i in self.__bestellungen:
            bestellungen += i
        print(bestellungen)
        return self.__Vorname + ',' + self.__Nachname + ',' + bestellungen

    def get_v_name(self):
        return self.__Vorname

    def set_v_name(self, vorname):
        self.__Vorname = vorname

    def get_name(self):
        return self.__Nachname

    def set_name(self, nachname):
        self.__Nachname = nachname

    def get_bestell(self):
        return self.__bestellungen

    def set_bestell(self, bestell):
        """
        Fugt eine Bestellung hinzu.
        """
        self.__bestellungen.append(bestell)

    def print_Ben(self):
        """
        Print alles uber ein Benutzer.
        """
        print(self.get_v_name()+' '+self.get_name())
        print(self.__bestellungen)
        print()
