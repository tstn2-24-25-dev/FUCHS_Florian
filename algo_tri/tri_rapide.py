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