import json

dataset = []
with open('data.json') as json_data:
    data = json.load(json_data)

for key,value in data.items():
    value[1] = value[0] * (value[1] / 100)
    data[key] = value

dataset = sorted(data.items())

print(dataset)

def sacADos_dynamique(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]

    for i in range(1, len(elements) + 1):
        for w in range(1, capacite + 1):

            if elements[i-1][1][0] <= w:
                matrice[i][w] = max(elements[i-1][1][1] + matrice[i-1][w-elements[i-1][1][0]], matrice[i-1][w])
            else:
                matrice[i][w] = matrice[i-1][w]

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []
    elements_poids = 0
    while w >= 0 and n >= 0:
        e = elements[n-1]
        if matrice[n][w] == matrice[n-1][w-e[1][0]] + e[1][1]:
            elements_selection.append(e)
            elements_poids += e[1][0]
            w -= e[1][0]

        n -= 1

    return elements_poids,matrice[-1][-1], elements_selection

resultat_dynamique = sacADos_dynamique(500, dataset)
print('Coût total : ', resultat_dynamique[0] )
print('profits : ', resultat_dynamique[1] )
print('Actions achetées : ')
for i in range(len(resultat_dynamique[2])) :
    print(resultat_dynamique[2][i][0])
