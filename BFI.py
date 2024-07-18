

# positive kodierung = 1 bis 5
# negative kodierung => rekodierung = 6 - (1 bis 5)

import csv

def openInventory():                                        ### Ruft das Inventory aus der .csv Datei auf   
    inventory = []
    with open('BFI2.csv', newline='') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        rowCount = 0
        for row in csv_reader:
            if rowCount >= 60:
                break
            inventory.append(row[:6])
            rowCount += 1
    return inventory



skala = ["stimme überhaupt nicht zu", "stimme eher nicht zu", "teils, teils", "stimme eher zu", "stimme voll und ganz zu"]

inventory = openInventory()

for line in range(0,len(inventory)):
    print(inventory[line])
