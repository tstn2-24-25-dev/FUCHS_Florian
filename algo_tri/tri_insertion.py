def triInsertion(tab:list)->list:
    '''
    Description : La fontion triInsertion(tab) tri la liste tab en 
    utilisant la methode de trie par Insertion :
    Le tri par insertion fonctionne comme un jeu de cartes : on insère chaque carte à sa place.
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
    for i in range(len(tab)-1):
        if tab[i]>tab[i+1]:
            ele=tab.pop(i+1)
            for j in range(i,-1,-1):
                if j==0 and ele<tab[j]:
                    tab.insert(j,ele)
                elif ele>tab[j-1] and ele<tab[j]:
                    tab.insert(j,ele)
    return(tab)

print(triInsertion([4,8,2,10,1,9,7,6,3,5]))