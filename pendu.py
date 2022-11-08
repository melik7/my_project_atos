# Code python pour le jeu du pendu 

from random import *


"""
This function implements the game of hangman, a word is randomly chosen from a pre-defined list 
and the player must guess this word
@return Returns an array filled with bouléan according to the size of the word to find
"""
def hangman():
    #Liste des mots à retouver
    words=["table", "dance", "anticonstitutionnellement", "juillet", "parapluie","tortue", "marcher", "manger", "bouger", "fleur"]
    
    #Mot à rechercher choisit aleatoirement
    word_to_find = words[randint(0,10)]

    while(cpt<len(word_to_find)):
        #Initialisation des variables 
        result=[]
        cpt=0
        index=[]

        letter = input("Veuillez choisir une lettre")
        if(letter in word_to_find):
            result.append(True) 
            
            #On récupère le ou les index de la lettre trouvée
            for i in range(len(word_to_find)):
                if(letter==word_to_find[i]):
                    index+=i
            result.extend(index, letter, cpt)
            #On gère l'affichage de la manche
            graphical_function(result)

        else:
            result.extend(False, index, letter, cpt)
            #On gère l'affichage de la manche
            graphical_function(result)
        cpt+=1