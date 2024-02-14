import csv

#отрытие файла
with open("space.csv", encoding='utf-8') as file:
    #превращение файла в словарь-список
    reader = list(csv.DictReader(file, delimiter='*',quotechar='"'))
    answer=list(reader[:1])

    #получение значений
    for ShipName, planet, direction in answer:
        ship_digit[ShipName] = int(ship_digit.get(Shipname[6], 0))
        ship_digit_again[ShipName] = int(ship_digit_again.get(ShipName[7], 0))
        name_length[planet] = len(name_length.get(planet))
        x[direction] = x.get(direction[0], 0)
        y[direction]= y.get(direction[1:], 0)

    #присвоение координат контакта
    for item in answer:
        if "0"  in str(item[-2]):
            item[-2]=f'{(ship_digit + x) if ship digit > 5 else -(ship_digit + x) * 4 + name_length)} \
                {(ship_digit_again + name_length + y) if ship_digit_again > 3 else -(ship_digit + y) * ship_digit_again }'
            
    #запись координат




