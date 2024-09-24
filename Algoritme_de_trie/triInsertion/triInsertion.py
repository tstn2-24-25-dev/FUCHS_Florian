def triInsertion(tab:list)->list:
    '''
    Description : La fontion triInsertion(tab) tri la liste tab en 
    utilisant la methode de trie par Insertion :
    Le tri par insertion fonctionne comme un jeu de cartes : on insère chaque carte à sa place.
    Voici les étapes successives du tri par insertion en utilisant des tableaux en Markdown avec de la mise en forme en gras et des couleurs pour illustrer les déplacements des éléments dans le tableau.
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
    
    
    
    
    
