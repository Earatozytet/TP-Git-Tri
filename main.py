import tkinter as tk
import random
import bulles, insertion, selection

# import re
# PATTERN = r"^-?\d*\.?\d*$" # NE PAS MODIFIER

Pqfpagmseevtm = 'ComicSansMS' #police qui fait plaisir à gaspard même si elle est vraiment très moche
dico_methode = {
    "Tri à bulle" : bulles.bulles,
    "Tri par insertion " : insertion.insertion,
    "Tri par selection " : selection.selection
}
def lancer_tri():
    """fonction qui lance le tri grace aux fonctions codé"""
    print("Tri lancé")
    if not entree.get("1.0",'end-1c') :
        resultat.config(state="normal")
        resultat.delete("1.0", "end")
        resultat.insert("1.0", "Liste vides")
        resultat.config(foreground="red", state="disabled")
    else :
        liste_nombres = [float(i) for i in entree.get("1.0",'end-1c').split(",")]
        algo_utiliser = algo.get()
        liste_triee = dico_methode[algo_utiliser](liste_nombres)
        resultat.config(state="normal",foreground=entree.cget("foreground"))
        resultat.delete("1.0", "end")
        resultat.insert("1.0", ", ".join(str(element) for element in liste_triee))
        resultat.config(state="disabled")

def is_entry_valid(entry, negatif_ok = True):
    """
    Vérifie si la chaine de caractère entry est composé uniquement de chiffres et éventuellement d'un '-'
    au début si negatif_ok est égal à True

    Keyword arguments:
    entry -- str, la chaine pour laquelle il faut vérifier si c'est une chaine composé de chiffres
    negatif_ok -- bool, indique s'il faut autoriser les '-' au début de la chaine (default True)
    """
    return len([e for index, e in enumerate(entry) if not e.isdigit() and not (negatif_ok and index==0 and e=="-")]) == 0

def generer_liste():
    # if re.match(PATTERN, nb_element.get()) is not None and \
    #     re.match(PATTERN, min_element.get()) is not None and \
    #     re.match(PATTERN, max_element.get()) is not None:
    if (is_entry_valid(nb_element.get().strip(), negatif_ok=False) and
            is_entry_valid(min_element.get().strip()) and
            is_entry_valid(max_element.get().strip())):
        nb = int(nb_element.get()) if nb_element.get() != "" else 2
        mini = int(min_element.get()) if min_element.get() != "" else 0
        maxi = int(max_element.get()) if max_element.get() != "" else 1

        if type_element.get() == "float":
            liste = [random.random() for i in range(nb)]
        else:
            liste = [random.randint(mini, maxi) for i in range(nb)]

        entree.delete("1.0", "end")
        entree.insert("1.0", ", ".join(str(element) for element in liste))

# création fenêtre
root = tk.Tk()
root.geometry("300x600")
root.title("Algorithmes de tri de NSI")

frame1 = tk.Frame(root)
frame1.pack(pady=5)

tk.Label(frame1,text="Générer une liste aléatoire :",font=Pqfpagmseevtm).grid(row=0, column=0, columnspan=5)

tk.Label(frame1, text="Nombre :", font=Pqfpagmseevtm).grid(row=1, column=0)
nb_element = tk.Entry(frame1, width=5, font=Pqfpagmseevtm)
nb_element.grid(row=1, column=1)

tk.Label(frame1, text="Type :", font=Pqfpagmseevtm).grid(row=2, column=0)
type_element = tk.StringVar(value="int")
menu_type_element = tk.OptionMenu(frame1, type_element, "int", "float")
menu_type_element.config(font=Pqfpagmseevtm)
menu_type_element["menu"].config(font=Pqfpagmseevtm)
menu_type_element.grid(row=2, column=1)

tk.Label(frame1, text="Min :", font=Pqfpagmseevtm).grid(row=1, column=3)
min_element = tk.Entry(frame1, width=5, font=Pqfpagmseevtm)
min_element.grid(row=1, column=4)

tk.Label(frame1, text="Max :", font=Pqfpagmseevtm).grid(row=2, column=3)
max_element = tk.Entry(frame1, width=5, font=Pqfpagmseevtm)
max_element.grid(row=2, column=4)

bouton_random = tk.Button(frame1,text="Générer",font=Pqfpagmseevtm,command=generer_liste)
bouton_random.grid(row=3, column=0, columnspan=5)


tk.Label(root, text="Liste à trier                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           :", font=Pqfpagmseevtm).pack()
entree = tk.Text(root,width=25,height=8,bd=1,relief="solid", highlightthickness=0,font=Pqfpagmseevtm)
entree.pack()

algo = tk.StringVar(value=list(dico_methode.keys())[0])
tk.Label(root, text="Méthode :",font=Pqfpagmseevtm).pack()

frame2 = tk.Frame(root)
frame2.pack()
menu_des_algo = tk.OptionMenu(frame2, algo, *dico_methode.keys())
menu_des_algo.config(font=Pqfpagmseevtm)
menu_des_algo["menu"].config(font=Pqfpagmseevtm)
menu_des_algo.pack(side="left")

bouton_tri = tk.Button(frame2,text="Trier",bg="#0992E6",fg="white",command=lancer_tri,font=Pqfpagmseevtm,)
bouton_tri.pack(side="left")
resultat = tk.Text(root,width=25,height=8,bd=1,relief="solid",highlightthickness=0,font=Pqfpagmseevtm,)
resultat.config(state="disabled")
resultat.pack()

root.mainloop()
