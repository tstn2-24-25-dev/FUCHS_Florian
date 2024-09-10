def recup_ocurence(lignes : str):
    for i in lignes:
         i.split(" ")

        



def inventaire(chemin : str):
    with open(chemin, 'r') as donne:
        lignes=donne.readlines()
        stock=lignes.pop(0)
        ocurence=recup_ocurence(lignes)
        affiche_res(ocurence)

        
