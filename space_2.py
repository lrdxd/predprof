import csv

with open("space.csv", encoding = 'utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='*'))
    for i in range(len(reader)):
        j = i-1
        key = reader[i]
        while int(reader[j]['ShipName'][4:]) < int(key['ShipName'][4:]) and j >= 0:
            reader[j+1] = reader[j]
        reader[j+1] = key

    count = 1
    for ship in reader:
        ship_name = ship['ShipName']
        print(ship_name)
        count += 1
        if count == 10:
            break
