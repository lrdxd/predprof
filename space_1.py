import csv
#отрытие файла
with open("space.csv", encoding='utf-8') as file:
    #превращение файла в словарь-список
    reader = list(csv.DictReader(file, delimiter='*',quotechar='"'))




