def triSelection(tab:list)->list:
    '''
    Description : La fontion triSelection(tab) tri la liste tab en 
    utilisant la methode de trie par selection : 
    a chaque etape, mettre le plus petit element a la bonne position
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
    for i in range(len(tab)):
        minI=indiceMin(tab,i)
        min=tab.pop(minI)
        tab.insert(i,min)
    return tab

def indiceMin(tab : list, j : int)->int:
    minI=j
    for i in range(j,len(tab)):
            if i<len(tab)-1:
                if tab[i]<tab[minI]:
                    minI = i
    return minI

if __name__=="__main__":
    help(triSelection)
    print(triSelection([4,8,2,10,1,9,7,6,3,5]))