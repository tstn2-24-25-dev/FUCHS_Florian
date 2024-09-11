def recup_ocurence(lignes : str):
    ocurence={}
    for i in lignes:
        i=i.split(" ")
        ocurence[i[0]] = int(i[1])
    return ocurence

def max_occurence(ocurence : dict):
    maxi=max(ocurence.values())
    maxs=""
    for keys in ocurence.keys():
        if ocurence[keys] == maxi:
            maxs+=f"{keys} "
    return maxs

def inventaire(chemin : str):
    with open(chemin, 'r') as donne:
        lignes=donne.readlines()
        nb_prop=lignes.pop(0)
        limit=nb_prop//2
        lignes.pop(0)
        ocurence=recup_ocurence(lignes)

        print(max_occurence(ocurence))
inventaire("Blockchain\\input1.txt")
inventaire("Blockchain\\input2.txt")