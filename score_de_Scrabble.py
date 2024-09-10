def recup_score_letre(score_str : str ):
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

def score_Scrabble(chemin : str):
    with open(chemin, 'r') as donne:
        lignes=donne.readlines()
        score=recup_score_letre(lignes[0])
        mots_sc={}
        mots=[]
        for i in range(1,len(lignes)):
            mots.append(lignes[i])
            mots_sc[lignes[i]] = calc_mot(lignes[i],score))
score_Scrabble("test.txt")

        
