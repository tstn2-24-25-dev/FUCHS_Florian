from random import shuffle
def bogo_sort(tab:list):
    while not trier(tab):
        shuffle(tab)
        print(tab)
    return(tab)

def trier(tab:list):
    tri=True
    for i in range(len(tab)-1):
        if tab[i]>tab[i+1]:
            tri = False
    return tri

print(bogo_sort([5,4,48,2,6,3,4,78,65,42,10]))