from pages import *


class GUI(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, *kwargs)
        self.title = 'BillsOrganizer'

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.screens = {}

        meni = Menu(container)

        mm = Menu(meni, tearoff=0)
        meni.add_cascade(menu=mm, label='Menu')
        mm.add_command(label='Start screen', command=lambda: self.show_page(StartScreen))
        mm.add_command(label='Find bills', command=lambda: self.show_page(Sorting))
        mm.add_command(label='Edit Bill', command=lambda: self.show_page(EditPage))
        mm.add_command(label='About', command=lambda: self.about_app())
        mm.add_separator()
        mm.add_command(label='Exit', command=self.destroy)

        Tk.config(self, menu=meni)

        for s in (StartScreen, Sorting, EditPage):
            screen = s(container, self)
            self.screens[s] = screen
            screen.grid(row=0, column=0, sticky='nsew')

        self.show_page(StartScreen)

    def show_page(self, container):
        """
        Function for page that will display on the screen
        :param container: container for the page
        """
        screen = self.screens[container]
        screen.tkraise()

    def about_app(self):
        messagebox.showinfo(title='Bill Paying App', message='made by:\nNemanja Novakovic\nnemanjalfc89@gmail.com')

