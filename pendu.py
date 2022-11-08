
def graphical_function(answer= False, result = [], letter = None, count= None):
    word_size = len(result)
    table = [" _ " for i in range(word_size)]
    print(table)
    print("O" * count, "-" * (10-count))
    if answer == False:
        print("O" * count)
    if answer == True:
        all_index = []
        for i,j in enumerate(result):
            if i == True:
                all_index.append(j)
        for index in all_index:
            table[index] = letter
        print(table)

    


# Exemple de fonctionnement 

tab = [True, False, False, False]
graphical_function(answer=True, result =tab , letter="A", count = 5)


