import tkinter 
from client.gui_app import Frame,barra_menu


def main():
    root = tkinter.Tk()
    root.title("Catálogo de películas")
    root.iconbitmap('img/claqueta.ico')
    # size of window
    root.resizable(0,0)

    #Call function barra_menu
    barra_menu(root)

    app = Frame(root = root)

    app.mainloop()

if __name__== '__main__':
    main()