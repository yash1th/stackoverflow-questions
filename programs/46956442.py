import sys
def readfile(fname):
    txt = open(fname)
    txt1 = txt.read()
    new_list = []
    for i in txt1:
        split_list = i.strip().split(',')
        print(split_list)
        #new_list.append({'Car': split[0], 'Seat': int(split[1]), 'cost': int(split[2])})
readfile('car.txt')