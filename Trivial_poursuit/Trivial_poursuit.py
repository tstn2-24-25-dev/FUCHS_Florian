from random import randint
def init_test():
    with open("./Trivial_poursuit/test", "w") as donne:
        nb_ligne=randint(10,50)
        for i in range(nb_ligne):
            donne.write(str(randint(1,6))+"\n")
def Trivial_puorsuit(chemin:str):
    init_test()
    with open(chemin, "r") as donne:
        lignes=donne.readlines()
        cj1=0
        lst_couleur=["violet", "orange" , "jaune" , "vert" , "rose" , "bleu"]
        for lancer in range(len(lignes)):
            cj1=(cj1+int(lignes[lancer]))%6
            # test pour verifier (tout les lancer étape par étape):
            # print(f"Lancer {lancer} : {lignes[lancer]} => {lst_couleur[cj1]}")
    print(lst_couleur[cj1])
Trivial_puorsuit("./Trivial_poursuit/test")