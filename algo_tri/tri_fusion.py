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
    print(f"tab : {tab} tab1 : {tab1}, tab2 : {tab2}, mid: {mid}, len {len(tab)}")
    return ranger(tab1,tab2)
def ranger(tab1:list, tab2:list):
    print(f"tab1 : {tab1}, tab2 : {tab2}")
    for i in range(len(tab1)):
        print(f"i {i},{tab1[i]}")
        for j in range(len(tab2)):
            print(f"j {j},{tab2[j]}")
            if tab1[i]>tab2[j]:
                print("insert")
                tab1.insert(i,tab2[j])
                print(tab1)
            if i==len(tab1)-1:
                print("insert def")
                tab1.insert(i+1,tab2[j])
                print(tab1)
    return tab1

if __name__=="__main__":
    help(triFusion)
    print([2, 10, 1][1:])
    print(triFusion([4,8,2,10,1,9,7,6,3,5]))