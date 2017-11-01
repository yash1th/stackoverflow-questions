import csv
import itertools
while 1:
    z = 'User1.csv'
    RUN1 = False
    RUN2 = False
    with open(z, 'r') as f:
        Line = csv.reader(f)
        for Line in itertools.islice(f, 1, 3):
            print('newline2')
            RUN1 = True
        if RUN1 == False:
            for Line in itertools.islice(f, 0, 1):
                print('newline1')
                RUN2 = True
            if RUN2 == False:
                print('newline0')   
    break