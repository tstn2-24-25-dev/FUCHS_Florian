def triSelection(tab:list)->list:
    '''
    Description : La fontion triSelection(tab) tri la liste tab en 
    utilisant la methode de trie par selection : 
    À chaque étape, mettre le plus petit élément à la bonne position
    Parametre : tab : list : IN/OUT
    Sorti : tab : list
    Precondition : tab doit être une list d'entier
    Postcondition : tab est modifier
    '''
    assert type(tab)==list ,"tab doit être une list"
    if len(tab)==0:
        return []
    else :
        assert type(tab[0])==int,"tab doit être une list d'entier"
    min=tab[-1]
    tabclone=tab[:]
    for i in range(len(tab)):
        min=tab[-1]
        for e in tabclone:
            if e<min:
                min = e
        tabclone.remove(min)
        tab.remove(min)
        tab.insert(i,min)
    return tab