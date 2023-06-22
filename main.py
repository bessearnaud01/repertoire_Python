from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror, showinfo
from listedesinscrits import FunctionlisteInscrits


class Personnage():

    def __init__(self, prenom, nom, photo):
        self.nom = nom
        self.prenom = prenom
        self.photo = photo

    # cette fontion permet de tester si l'utilisateur existe
    def __eq__(self, other):
        return self.prenom == other.prenom and self.nom == other.nom


def parcourir():
    global image_Name
    imn = askopenfilename(initialdir="/", title="selectionner une image",
                          filetypes=(("png files", "*.png"), ("jpeg files", "*.jpeg")))
    # On teste si le fichier existe ou pas
    if imn:
        image_Name = imn
    if image_Name:
        texte = image_Name.split("/")  # Elle sert à recuperer le dernier élément pour mettre dans le tableau
        photoEntre.configure(text=".../" + texte[-1])


def existe(liste, val):
    for i in range(len(liste)):
        if liste[i].__eq__(val):
            return 1
    return 0


def valider():
    global ListePersonne, image_Name
    photo = image_Name
    if prenomEntre.get() and nomEntre.get() and photo:
        np = Personnage(prenomEntre.get(), nomEntre.get(), photo)  # np = classe personne si
        # on teste si l'utilisateur existe
        if existe(ListePersonne, np):
            showerror(title="Formulaire d'invalidité", message="L'utilisateur existe déja !")
        else:
            ListePersonne.append(np)
            showinfo(title="Validation réussie", message="a bien été ajouter".format(prenomEntre.get()))
    else:
        showerror(title="Formulaire d'invalidité", message="Tous les champs doit être renseigner!")


def reinitialiser():
    global image_Name

    prenomEntre.delete(0, END)
    nomEntre.delete(0, END)
    image_Name = ''
    photoEntre.configure(text="Aucun image selectionner")


image_Name, ListePersonne = '', []

fen = Tk()
fen.geometry("290x290+400+150")
fen.title("page d'inscription")
contenu = Canvas(fen, bg="#FF7800")

fontLabel = 'arial  11 bold'
fontEntre = 'arial 10 bold'

nom = Label(contenu, text="Nom :", font=fontLabel, bg="#FF7800")
prenom = Label(contenu, text="Prénom :", font=fontLabel, bg="#FF7800")
photo = Label(contenu, text="Photo :", font=fontEntre, bg="#FF7800")
validation = Label(contenu, text="Entrer vos information ici :", font=("Helvetica", 10, "bold"), bg="#FF7800")

nomEntre = Entry(contenu, font=fontEntre, width=22)
prenomEntre = Entry(contenu, font=fontEntre, width=22)

photoEntre = Label(contenu, text="Sélectionner la photo :", bg="#FF7800")

ButtonParcourir = Button(contenu, text="Pr", bg="lightgrey", command=parcourir)

validation.grid(row=0, column=1, columnspan=2)
nom.grid(row=1, column=0, sticky=E, padx=5, pady=5)
prenom.grid(row=2, column=0, sticky=E, padx=5, pady=5)
photo.grid(row=3, column=0, sticky=E, padx=5, pady=5)

nomEntre.grid(row=1, column=1, sticky=E, padx=5, pady=5)

nomEntre.grid(row=1, column=1, sticky=E, padx=5, pady=5)
prenomEntre.grid(row=2, column=1, sticky=E, padx=5, pady=5)
photoEntre.place(x=86, y=100)
ButtonParcourir.grid(row=3, column=1, sticky=E, padx=5, pady=5)

Button2 = Button(contenu, text="Valider", bg="lightgrey", width=20, command=valider)

Button3 = Button(contenu, text="reinitialiser", bg="lightgrey", command=reinitialiser, width=20)

Button4 = Button(contenu, text="Voir la liste", command=lambda: FunctionlisteInscrits(fen, ListePersonne),
                 bg="lightgrey", width=20)

Button2.grid(row=4, column=1, padx=5, pady=5, sticky=W)
Button3.grid(row=5, column=1, padx=5, pady=5, sticky=W)
Button4.grid(row=6, column=1, padx=5, pady=5, sticky=W)
contenu.place(x=0, y=10, width=400, height=600)

contenu.mainloop()
