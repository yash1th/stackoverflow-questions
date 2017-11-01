with open("lengths.txt",'r') as a, open("widths.txt",'r') as b:
    count = 1
    for x, y in zip(a, b):
        x = int(x.strip())
        y = int(y.strip())
        print('Rectangle {} : {} x {} = {}'.format(count, x, y, x*y))
        count += 1
        #print("length: {0}\twidth: {1}".format(x, y))