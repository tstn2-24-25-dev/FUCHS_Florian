import io
def score_Scrabble(chemin : str):
    with open(chemin, 'r') as donne:
        for i in donne.readlines():
            print(i)
score_Scrabble("test.txt")

        
