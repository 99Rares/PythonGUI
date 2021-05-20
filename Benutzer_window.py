import tkinter as tk
from tkinter import messagebox

from Benutzer_Class import Benutzer
from Pages import Page
from gem import Gemeinsam as r


# noinspection PyShadowingBuiltins
class BenutzerWindow(Page):

    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        # create Window
        self.__benutzer = []
        self.inputBenData()

        # Benutzer Name
        self.__ben_name = tk.StringVar()
        label_Ben_Name = tk.Label(self, text="Benutzer Name: ", font='bold,14', pady=20)
        label_Ben_Name.grid(row=0, column=0)
        benName_entry = tk.Entry(self, textvariable=self.__ben_name)
        benName_entry.grid(row=0, column=1)

        # Benutzer Vorname
        self.__ben_vname = tk.StringVar()
        label_Ben_Vname = tk.Label(self, text="Benutzer Vorname: ", font='bold,14', pady=20)
        label_Ben_Vname.grid(row=1, column=0)
        benVname_entry = tk.Entry(self, textvariable=self.__ben_vname)
        benVname_entry.grid(row=1, column=1)

        # Button
        add_btn = tk.Button(self, text='Add Benutzer', command=self.addItem)
        add_btn.grid(row=2, column=0, pady=20)

        del_btn = tk.Button(self, text='Delete Benutzer', command=self.delItem)
        del_btn.grid(row=2, column=1)

        update_btn = tk.Button(self, text='Update Benutzer', command=self.updateItem)
        update_btn.grid(row=2, column=2)

        save_btn = tk.Button(self, text='Save', command=self.save)
        save_btn.grid(row=2, column=4)

        help_btn = tk.Button(self, text='Help', command=self.help)
        help_btn.grid(row=6, column=3, pady=10)

    @property
    def ben_name(self):
        return self.__ben_name

    @property
    def ben_vname(self):
        return self.__ben_vname

    def addBenutzer_Txt(self, data):
        """
        Liest aus die gelesen Daten
        """
        for benutzer in data:
            benutzer = benutzer.replace('\n', '').split(',')
            benutzer[2] = benutzer[2].split(";")
            self.__benutzer.append(Benutzer(benutzer[0], benutzer[1], benutzer[2]))

    def inputBenData(self):
        """
        Liest aus ein Datei
        """
        benutzer = open("Benutzer.txt", 'r')
        benData = benutzer.readlines()
        self.addBenutzer_Txt(benData)

    def benutzer_finden(self, name):
        print(name)
        id_ben = 0
        for i in self.__benutzer:
            print(i.get_v_name())
            if i.get_v_name() == name:
                return id_ben
            id_ben += 1
        return -1

    def updateName(self, oldName, newName):
        """
        aktualisiert den Nachnamen
        """
        ID = self.benutzer_finden(oldName)
        print(ID)
        if ID == -1:
            ID = 'None'
        else:
            pass
        try:

            self.__benutzer[ID].set_name(newName)
            print("Update durchgefugt", 'blue')
        except:
            print("Update NICHT durchgefugt", 'red')

    def del_ben(self, name):
        """
        Loscht ein Benutzer
        """
        ID = self.benutzer_finden(name)
        if ID == -1:
            ID = 'None'
        else:
            pass
        try:
            del self.__benutzer[ID]
            print(("Loschung durchgefugt", 'blue'))
        except:
            print(("Loschung NICHT durchgefugt", 'red'))

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

    @property
    def benutzer(self):
        return self.__benutzer

    def addItem(self):
        v_name = self.ben_vname.get()
        name = self.ben_name.get()
        new_bentzer = Benutzer(v_name, name)
        self.__benutzer.append(new_bentzer)
        messagebox.showinfo("Information", "Benutzer eingefuhrt")
        print("ok")

    def delItem(self):
        self.del_ben(self.ben_vname.get())
        messagebox.showinfo("Information", "Delete durchgefuhrt")
        print('Delete')

    def updateItem(self):
        self.updateName(self.ben_vname.get(), self.ben_name.get())
        messagebox.showinfo("Information", "Update durchgefuhrt")
        print('Update')

    def clearItem(self):
        print('Clear')

    def save(self):
        print('save')
        self.outputBenutzerData()

    def help(self):
        help_pls= "Der Knopf 'Add Benutzer' fugt ein Benutzer hinzu(Name und Vorname wehlen)\n"+"Der Knopf 'Delete "\
                    "Benutzer' Lost ein Benutzer(Name und Vorname wehlen)\n"+"Der Knopf ' Update Benutzer' " \
                    "aktualisiert den Namen des Benutzers(Name und Vorname wehlen)\n" \
                    + "Das Knoplf 'Save'speigert in der Datei "
        messagebox.showinfo("Help",help_pls)
