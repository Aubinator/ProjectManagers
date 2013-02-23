from tkinter import *



def hello():
    print ("salut Aubin!")

def Menus(root):
    menubar = Menu(root)
    # create a pulldown menu for the file menu
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Liste Projet", command=hello)
    filemenu.add_command(label="Infos Projet", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Fermer", command=root.quit)
    menubar.add_cascade(label="Fichier", menu=filemenu)

    # let's create de edition menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Ajout Entreprise", command=hello)
    editmenu.add_command(label="Ajout Projet ", command=hello)
    editmenu.add_command(label="Gerer Developpeur", command=hello)
    editmenu.add_command(label="Gerer", command=hello)
    editmenu.add_command(label="Gerer Developpeur", command=hello)
    menubar.add_cascade(label="Edition", menu=editmenu)

    #and the last one the elp menu
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="A Propos", command=hello)
    menubar.add_cascade(label="Aide", menu=helpmenu)


    # display the menu
    root.config(menu=menubar)


