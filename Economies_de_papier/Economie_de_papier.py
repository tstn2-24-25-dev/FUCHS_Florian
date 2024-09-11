def Economie_de_papier(chemin:str):
    with open(chemin, "r") as donne:
        nb_page=1
        remplit=0
        lignes=donne.readlines()[0].split(" ")
        for i in lignes:
            if remplit+int(i)>10:
                remplit=int(i)
                nb_page+=1
            else:
                remplit+=int(i)
    print(nb_page)
            
Economie_de_papier(".\Economies_de_papier\input1.txt")
Economie_de_papier("./Economies_de_papier//input2.txt")
Economie_de_papier("./Economies_de_papier//input3.txt")
Economie_de_papier("./Economies_de_papier//input4.txt")
Economie_de_papier("./Economies_de_papier//input5.txt")