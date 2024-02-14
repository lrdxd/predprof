import csv
#отрытие файла
with open("space.txt") as file:
    reader=csv,reader(file,delimiter='*')
    '''itog=list(reader[:-1])'''
    for location in reader:
        x_cord, y_cord=location['coord_place'].split()

