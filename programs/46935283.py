import csv
from itertools import zip_longest

total_list = []
with open('testfile_test.txt') as input_file:
    for line in input_file:
        if "Car Details" in line:
            car_details = dict.fromkeys(['vin','modelCode','color','chassis','Starting Location','Owning Organization','Final Organization'],'')
            split_line = line.split(',')
            for text in split_line[1:]:
                value= text.strip().split(' ',1)
                if len(value)>1:
                    car_details[value[0]]=value[1]
            total_list.append(car_details)

with open("newfilename.csv", 'a') as outcsv:   
    writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
    writer.writerow(['Vin', 'Model Code', 'Colour', 'Chassis', 'Starting Location', 'Owning Organization', 'Final Organization'])
    for detail in total_list:
        writer.writerow([detail['vin'],detail['modelCode'],detail['color'],detail['chassis'],detail['Starting Location'],detail['Owning Organization'],detail['Final Organization']])