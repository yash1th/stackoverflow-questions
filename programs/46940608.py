# import csv

# with open('test.csv', 'r') as csvfile:
#     reader=csv.reader(csvfile, delimiter = ';')
#     for r in reader:
#         print(r)

# class Element:
#     def __init__(self, name, period, group):
#         self.name = name
#         self.period = period
#         self.group = group

# hydrogen = Element('hydrogen', 1, 1)
# # this prints the attribute names and values
# print(hydrogen.__dict__)

def getFile():
    #prose = str(input('Please enter the file path for your text file: '))

    dictionary = {}

    infile = open('test.csv', 'r')
    line_num = 1
    for line_num, line in enumerate(infile, start = 1):
        dictionary[line_num] = line
        print(dictionary)
    infile.close()

getFile()