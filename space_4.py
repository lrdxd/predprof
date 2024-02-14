import csv
import string
#выдача кораблю пароля
def credentials(s: string):
    ship = s.split()
    return f'{ship[0]}_{ship[1][0]}{ship[2][0]}'

#список кораблей с паролями
ship_passes = []

#проход по файлу и присвоение пароля
with open("space.csv", encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter='*', quotechar='"'))
    for row in reader:
        row['password']=credentials(row['ShipName'])

#запись нового файла
with open("space_uniq_password.csv", 'w', newline='', encoding='utf-8') as file:
    w = csv.DictWriter(file, fieldnames=['ShipName','planet','coord_place','direction', 'password'])
    w.writeHeader()
    w.writerows(shis_passes)



