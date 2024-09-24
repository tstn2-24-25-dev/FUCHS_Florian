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
    return ranger(tab2,tab1)
def ranger(tab1:list, tab2:list):
    print(f"tab1 : {tab1}, tab2 : {tab2}")
    id=0
    idp=1
    print(f"len {len(tab1)}")
    for i in range(len(tab1)+1):
        print(f"i {i},{tab1[i]}")
        e=tab1[i]
        for j in range(id,len(tab2)):
            print(f"j {j},{tab2[j]}, id {id}, idp {idp}")
            if i==len(tab1):
                print("insert def")
                print(tab1)
                tab1.insert(i+idp,tab2[j])
                print(tab1)
                idp+=1
                id=j+1
            if e>tab2[j]:
                print("insert")
                print(tab1)
                tab1.insert(tab1.index(e),tab2[j])
                print(tab1)
                id=j+1
    return tab1

if __name__=="__main__":
    help(triFusion)
    print(triFusion([4,8,2,10,1,9,7,6,3,5]))