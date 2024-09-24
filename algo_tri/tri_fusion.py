def triFusion(tab:list)->list:
    '''
    Description : La fontion triInsertion(tab) tri la liste tab en 
    utilisant la methode de trie Fusion
    Parametre : tab : list : IN/OUT
    Sorti : tab : list
    Precondition : tab doit être une list d'entier
    Postcondition : tab est modifier
    '''
    assert type(tab)==list ,"tab doit être une list"
    if len(tab)==0 or len(tab)==1:
        return tab
    else :
        assert type(tab[0])==int,"tab doit être une list d'entier ou vide"
    mid=len(tab)//2
    tab1=triFusion(tab[:mid])
    tab2=triFusion(tab[mid:])
    return ranger(tab2,tab1)
def ranger(tab1:list, tab2:list):
    id=0
    len1=len(tab1)
    for i in range(len(tab1)):
        e=tab1[i]
        for j in range(id,len(tab2)):
            ajout=False
            if e>tab2[j]:
                tab1.insert(tab1.index(e),tab2[j])
                id=j+1
                ajout=True
            if i==len1-1 and not ajout:
                tab1.insert(len(tab1),tab2[j])
                id=j+1
    return tab1

if __name__=="__main__":
    help(triFusion)
    print(triFusion([4,8,2,10,1,9,7,6,3,5]))