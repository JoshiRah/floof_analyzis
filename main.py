import requests
import matplotlib.pyplot as plt

rounds = 10
floofs = []

floofNames = []

for i in range(123):
    floofNames.append('')

a = 0
b = 1

for i in range(123):
    floofNames[a] = b
    b += 1
    a += 1


for i in range(123):
    floofs.append(0)


for i in range(rounds):

    response = requests.get("https://randomfox.ca/floof/")
    fox = response.json()

    link = fox['link']
    splittedLink = link.split('=')
    floofNumber = splittedLink[1]


    floofs[int(floofNumber)] += 1



    print('Fortschritt', i, 'von', rounds-1)


plt.bar(floofNames, floofs, label='Count of floof')
plt.legend(loc='upper left')
plt.show()