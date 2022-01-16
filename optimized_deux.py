import csv

dataset = []
with open('dataset2.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        if row[0].split(',')[0] == 'name' or float(row[0].split(',')[1]) <= 0 or float(row[0].split(',')[2]) <= 0 :
            continue
        dataset.append((row[0].split(',')[0], int(float(row[0].split(',')[1])*100), int(float(row[0].split(',')[2])/100*float(row[0].split(',')[1])*100) ))

# Solution optimale - programmation dynamique
def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):

            if elements[i-1][1] <= w:
                matrice[i][w] = max(elements[i-1][2] + matrice[i-1][w-elements[i-1][1]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []
    elements_poids = 0
    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1]] + e[2]:
            elements_selection.append(e)
            elements_poids += e[1]
            w -= e[1]

        n -= 1

    return elements_poids/100,matrice[-1][-1]/100, elements_selection

resultat_dynamique = sacADos_dynamique(50000, dataset)
print('Coût total : ', resultat_dynamique[0] )
print('profits : ', resultat_dynamique[1] )
print('Actions achetées : ')
for i in range(len(resultat_dynamique[2])) :
    print(resultat_dynamique[2][i][0])
