from tkinter import *
from PIL import Image, ImageTk


def FunctionlisteInscrits(fenetre, liste):
    newFen = Toplevel(fenetre)
    newFen.geometry("290x290+400+150")
    newFen.title("page d'inscription")

    listeCant = Canvas(newFen)

    resultat = Label(listeCant, text=" La liste des utilisateurs :", font=("Helvetica", 10, "bold"), fg="black"
                     )

    nom = Label(listeCant, text="Nom:", font=("Helvetica", 10, "bold"), fg="black")

    prenom = Label(listeCant, text="Prénom :", font=("Helvetica", 10, "bold"), fg="black")

    photo = Label(listeCant, text="Photo :", font=("Helvetica", 10, "bold"), fg="#FF7800")
    status = Label(listeCant, text="Aucun n'inscrit pour le moment :", font=("Helvetica", 10, "bold"),fg="black" )

    listeCant.place(x=7,y=40,height=200,width=250)
    resultat.grid(row=0, column=1, columnspan=3)
    nom.grid(row=1, column=3, padx=5, pady=5)
    prenom.grid(row=1, column=2, padx=5, pady=5)
    photo.grid(row=1, column=1, padx=5, pady=5)
    status.grid(row=4, columnspan=3, padx=5, pady=5)

    # si la liste n'est pas vide
    if liste:
        r = 2
        for p in liste:
            photoLabel = Label(listeCant, height=50)
            img = Image.open(p.photo)
            img = img.resize((80, 80), Image.ANTIALIAS)
            photoLabel.img = ImageTk.PhotoImage(img)
            photoLabel.configure(image=photoLabel.img)

            nm = Label(listeCant, text=p.nom, font=("Helvetica", 10, "bold"),fg="black" )
            prnm = Label(listeCant, text=p.nom, font=("Helvetica", 10, "bold"), fg="black")

            photoLabel.grid(row=r, column=1)
            nm.grid(row=r, column=2)
            prnm.grid(row=r, column=3)
            listeCant.create_line(9, 55, 355, 55, width=1, fill='#FF7800')
            r += 1
            status.configure(text="{} inscrit pour le moment".format(len(liste)))

            status.grid(row=4, columnspan=3, padx=5, pady=5)

        newFen.mainloop()
