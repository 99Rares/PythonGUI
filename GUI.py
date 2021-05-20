import tkinter as tk
from Benutzer_window import BenutzerWindow
from film_window import FilmWindow
from gem_window import GemeinsamesWindow


class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        page1 = BenutzerWindow(self)
        page2 = FilmWindow(self)
        page3 = GemeinsamesWindow(self)
        buttonmenu = tk.Frame(self)
        container = tk.Frame(self)
        buttonmenu.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        page1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        page3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonmenu, text="BenutzerWindow", command=page1.lift)
        b2 = tk.Button(buttonmenu, text="FilmWindow", command=page2.lift)
        b3 = tk.Button(buttonmenu, text=" GemeinsamesWindow", command=page3.lift)

        b1.pack(side="left")
        b2.pack(side="left")
        b3.pack(side="left")

        page1.show()


if __name__ == "__main__":
    root = tk.Tk()
    root.configure(background='white')
    root.title('Online Shop')
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("700x400")
    root.mainloop()
