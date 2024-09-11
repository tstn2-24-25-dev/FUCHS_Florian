def parcour_ocurence(lignes : str, limit : int):
    adds=""
    for i in lignes:
        adds+=add_occurence(i,limit)
    return adds
def add_occurence(i : list, limit : int):
    i=i.split(" ")
    if int(i[1]) >= limit:
        return i[0]
    else: 
        return ""
def blockchain(chemin : str):
    with open(chemin, 'r') as donne:
        lignes=donne.readlines()
        nb_prop=lignes.pop(0)
        limit=int(nb_prop)/2
        lignes.pop(0)
        ocurence=parcour_ocurence(lignes,limit)
        print(ocurence)
blockchain("Blockchain\\input1.txt")
blockchain("Blockchain\\input2.txt")