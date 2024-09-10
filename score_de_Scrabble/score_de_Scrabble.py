def recup_score_letre(score_str : str):
    score={}
    sc_lst=score_str.split(" ")
    for l in range (0,len(sc_lst)-1,2):
        score[sc_lst[l]]=int(sc_lst[l+1])
    return score
        
def calc_mot(mot,score : dict):
    sc=0
    for i in mot:
            try :
                sc += score[i]
            except:
                 sc+=0
    return sc

def tri(list_mots : list):
    list_mots.sort(key=lambda a: a[1], reverse=True)
    return list_mots
def affiche_res(list_mots):
     for mot in list_mots:
          print(mot[0].replace("\n",""))

def score_Scrabble(chemin : str):
    with open(chemin, 'r') as donne:
        lignes=donne.readlines()
        score=recup_score_letre(lignes[0])
        mots=[]
        for i in range(1,len(lignes)):
            mots.append((lignes[i],calc_mot(lignes[i],score)))
        affiche_res(tri(mots))



score_Scrabble(input("entrer le chemins d'un fichier : "))

        
