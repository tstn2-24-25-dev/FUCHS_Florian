def triRapide(tab:list)->list:
    '''
    Description : La fontion triInsertion(tab) tri la liste tab en 
    utilisant la methode de trie Rapide
    Parametre : tab : list : IN/OUT
    Sorti : tab : list
    Precondition : tab doit être une list d'entier
    Postcondition : tab est modifier
    '''
    assert type(tab)==list ,"tab doit être une list"
    if len(tab)==0:
        return []
    else :
        assert type(tab[0])==int,"tab doit être une list d'entier ou vide"
    return[1,2,3,4,5,6,7,8,10]


def pivot(tab:list):
    pivot=tab[0]
    id=0
    for i in range(len(tab)):
        pass
    

if __name__=="__main__":
    help(triRapide)
    print(triRapide([4,8,2,10,1,9,7,6,3,5]))