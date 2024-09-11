def recup_ocurence(lignes : str):
   ocurence={}
   for i in lignes:
      i=i.split(" ")
      if not i[0] in ocurence.keys():
         ocurence[i[0]] = int(i[1])
      else :
         ocurence[i[0]] += int(i[1])
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
        lignes.pop(0)
        ocurence=recup_ocurence(lignes)
        print(max_occurence(ocurence))
inventaire("Inventaire\\test.txt")
inventaire("Inventaire\\test2")
inventaire("Inventaire\\test3")
        
