import json

dataset = []
with open('data.json') as json_data:
    data = json.load(json_data)

for key,value in data.items():
    value[1] = value[0] * (value[1] / 100)
    data[key] = value

dataset = sorted(data.items())

def sacADos_force_brute(capacite, elements, elements_selection = []):
    if elements:
        val1, lstVal1 = sacADos_force_brute(capacite, elements[1:], elements_selection)
        val = elements[0]
        if val[1][0] <= capacite:
            val2, lstVal2 = sacADos_force_brute(capacite - val[1][0], elements[1:], elements_selection + [val])
            if val1 < val2:
                return val2, lstVal2

        return val1, lstVal1
    else:
        return sum([i[1][1] for i in elements_selection]), elements_selection

cout_total = 0
resultats = sacADos_force_brute(500, dataset)
print("Actions achetées : ")
for i in  resultats[1] :
    cout_total += i[1][0]
    print(i[0])
print("Cout_total : ",cout_total)
print("Profits : ", resultats[0])