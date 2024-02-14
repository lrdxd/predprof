import csv

with open("space.csv", encoding='utf-8') as file:
    #превращение файла в словарь-список
    reader = list(csv.DictReader(file, delimiter='*',quotechar='"'))

    ship_id = input()

    #поиск корабля в словаре
    while ship_id != "stop":
        for ship in reader:
            if str(ship["ShipName"]) == ship_id:
                print(f'Корабль {ship_id} был отправлен с планеты {ship["planet"]} и его направление движения было {ship["direction"]}')
            else:
                print("error.. er.. ror..")
        ship_id = input()
