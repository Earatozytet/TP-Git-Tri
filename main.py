import tkinter as tk
import bulles, insertion, selection

Pqfpagmseevtm = 'ComicSansMS' #police qui fait plaisir à gaspard même si elle est vraiment très moche
dico_methode = {
    "Tri à bulle" : bulles.bulles,
    "Tri par insertion " : insertion.insertion,
    "Tri par selection " : selection.selection
}
def lancer_tri():
    """fonction qui lance le tri grace aux fonctions codé"""
    print("tri lancé")
    if not entree.get("1.0",'end-1c') :
        resulta.config(text="liste vide", fg = "red")
    else :
        liste_nombres = [float(i) for i in entree.get("1.0",'end-1c').split(",")]
        algo_utiliser = algo.get()
        liste_triee = dico_methode[algo_utiliser](liste_nombres)
        resulta.config(text=liste_triee, fg = "black")

root = tk.Tk()
root.geometry("300x400")
root.title("Trieur de NSI")

tk.Label(root, text="Liste à trier :", font=Pqfpagmseevtm).pack()
entree = tk.Text(root,width=25,height=8,bd=1,relief="solid", font=Pqfpagmseevtm)
entree.pack()

algo = tk.StringVar(value=list(dico_methode.keys())[0])
methode = tk.Label(root, text="Méthode : ",font=Pqfpagmseevtm)
methode.pack()

frame = tk.Frame(root)
frame.pack()
menu_des_algo = tk.OptionMenu(frame, algo, *dico_methode.keys())
menu_des_algo.config(font=Pqfpagmseevtm)
menu_des_algo.pack(side="left")
bouton = tk.Button(frame,text="Trier",bg="#0992E6",fg="white",command=lancer_tri,font=Pqfpagmseevtm,)
bouton.pack(side="left")

resulta = tk.Label(root, width=25,height=8, bd=1,relief="solid", font=Pqfpagmseevtm, anchor="nw")
resulta.pack()

root.mainloop()
