class Film:
    """
    Die Klasse ist fur die Filme des Online Shops.
    Die Klasse enthalt: den Konstruktor und get und set Funktionen fur alle Attribute.

    Attribute:
        Titel (string), Jahr (int), Wertung (int), Preis (int), Schauspieler (list)
    """

    def __init__(self, Titel, Jahr, Wertung,schauspieler, Preis):
        """
        Der Konstruktor der Klasse.

        Parameters:
            Titel (string), Jahr (int), Wertung (float), Preis (int), Schauspieler (list)
        """
        self.titel = Titel
        self.jahr = Jahr
        self.wertung = Wertung
        self.preis = Preis
        self.schauspieler = schauspieler

    def getTitel(self):
        return self.titel

    def getJahr(self):
        return self.jahr

    def getWertung(self):
        return self.wertung

    def getPreis(self):
        return self.preis

    def getSchauspieler(self):
        return self.schauspieler

    def setPreis(self, preis):
        self.preis = preis

    def print_filme(self):
        print(self.titel+' ; Jahr: ',end='')
        print(str(self.jahr)+ ' ; Wertung: ',end='')
        print(str(self.wertung)+ ' ; Preis: ',end='')
        print(str(self.preis))
        print('Actors: '+ str(self.schauspieler))
        print("\n")

    def hatSchauspieler(self, schauspieler):
        for sch in self.schauspieler:
            if sch == schauspieler:
                return True
        return False
