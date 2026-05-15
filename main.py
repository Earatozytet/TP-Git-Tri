import tkinter as tk
import bulles, insertion, selection

dico_methode = {
    "tri à bulle" : bulles.bulles,
    "tri par insertion " : insertion.insertion,
    "tri par selection " : selection.selection
}
def lancer_tri():
    """fonction qui lance le tri grace aux fonctions codé"""
    print("tri lancé")
    liste_nombres = [float(i.strip()) for i in entree.get().split(",")]
    algo_utiliser = algo.get()
    liste_triee = dico_methode[algo_utiliser](liste_nombres)
    resulta.config(text=liste_triee)

root = tk.Tk()
root.geometry("200x300")
root.title("Trieur de NSI")

tk.Label(root, text="Liste à trier").pack()
entree = tk.Entry(root)
entree.pack()

algo = tk.StringVar(value="tri à bulle")
tk.Label(root, text="Méthode : ").pack()
menu_des_algo = tk.OptionMenu(root, algo,*dico_methode.keys())
menu_des_algo.pack()

bouton = tk.Button(root, text="lancer le tri", command=lancer_tri)
bouton.pack()

resulta = tk.Label(root, text="",)
resulta.pack()

root.mainloop()
